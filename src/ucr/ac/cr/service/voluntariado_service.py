from src.ucr.ac.cr.model.voluntario import Voluntario
from src.ucr.ac.cr.model.actividad import Actividad
from src.ucr.ac.cr.model.participacion import Participacion
from src.ucr.ac.cr.model.dto import ParticipacionViewDTO
from datetime import datetime



class VoluntariadoService:

    def __init__(self, vol_repo, act_repo, part_repo):
        self.vol_repo = vol_repo
        self.act_repo = act_repo
        self.part_repo = part_repo

    # ----------- VOLUNTARIO -----------
    def register_voluntario(self, id, nombre, telefono, tipo, estado):

        if not id.strip():
            raise ValueError("El ID no puede estar vacío")

        if len(id) < 3:
            raise ValueError("El ID debe tener al menos 3 caracteres")

        if " " in id:
            raise ValueError("El ID no puede contener espacios")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not nombre.replace(" ", "").isalpha():
            raise ValueError(
                "El nombre solo debe contener letras"
            )

        nombre = nombre.title()

        if not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")

        if not telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números")

        if len(telefono) != 8:
            raise ValueError("El teléfono debe tener 8 dígitos")

        if tipo.lower() not in ["permanente", "ocasional"]:
            raise ValueError(
                "El tipo debe ser Permanente u Ocasional"
            )

        if estado.lower() not in ["activo", "inactivo"]:
            raise ValueError(
                "El estado debe ser Activo o Inactivo"
            )

        for voluntario in self.vol_repo.get_all():

            if voluntario.id == id:
                raise ValueError(
                    "Ya existe un voluntario con ese ID"
                )

            if voluntario.telefono == telefono:
                raise ValueError(
                    "Ya existe un voluntario con ese teléfono"
                )

        voluntario = Voluntario(
            id,
            nombre,
            telefono,
            tipo,
            estado
        )

        self.vol_repo.add(voluntario)

    def get_voluntarios(self):
        return self.vol_repo.get_all()

    def get_voluntario_by_id(self, voluntario_id):

        voluntario = self.vol_repo.get_by_id(voluntario_id)

        if voluntario is None:
            raise ValueError("Voluntario no encontrado")

        return voluntario

    # ----------- ACTIVIDAD -----------
    def register_actividad(self, id, nombre, fecha, ubicacion, capacidad_maxima):

        if not id.strip():
            raise ValueError("El ID no puede estar vacío")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía")

        try:
            capacidad_maxima = int(capacidad_maxima)

        except ValueError:
            raise ValueError("La capacidad máxima debe ser numérica")

        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor a 0")

        for actividad in self.act_repo.get_all():

            if actividad.id == id:
                raise ValueError("Ya existe una actividad con ese ID")

        try:
            fecha_convertida = datetime.strptime(fecha, "%Y/%m/%d")

        except ValueError:
            raise ValueError("La fecha debe tener formato YYYY/MM/DD")

        if fecha_convertida.date() < datetime.now().date():
            raise ValueError("La fecha no puede ser anterior al día actual")

        actividad = Actividad(id, nombre, fecha, ubicacion, capacidad_maxima)
        self.act_repo.add(actividad)

    def get_actividades(self):
        return self.act_repo.get_all()

    # ----------- PARTICIPACION -----------

    def register_participacion(self, id, voluntario_id, actividad_id, horas):

        if not id.strip():
            raise ValueError("El ID de participación no puede estar vacío")

        if len(id) < 3:
            raise ValueError("El ID debe tener al menos 3 caracteres")

        if " " in id:
            raise ValueError("El ID no puede contener espacios")

        if self.part_repo.exists(id):
            raise ValueError("Ya existe una participación con ese ID")

        if not self.vol_repo.exists(voluntario_id):
            raise ValueError("El voluntario no existe")

        voluntario = self.vol_repo.get_by_id(voluntario_id)

        if voluntario.estado.lower() == "inactivo":
            raise ValueError(
                "El voluntario está inactivo y no puede participar"
            )

        if not self.act_repo.exists(actividad_id):
            raise ValueError("La actividad no existe")

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        if horas > 24:
            raise ValueError("Las horas no pueden ser mayores a 24")

        for participacion in self.part_repo.get_all():

            if (participacion.voluntario_id == voluntario_id
                    and participacion.actividad_id == actividad_id):
                raise ValueError(
                    "El voluntario ya participa en esta actividad"
                )

        actividad = self.act_repo.get_by_id(actividad_id)

        if actividad.capacidad_maxima > 0:

            participantes_actuales = 0

            for participacion in self.part_repo.get_all():

                if participacion.actividad_id == actividad_id:
                    participantes_actuales += 1

            if participantes_actuales >= actividad.capacidad_maxima:
                raise ValueError(
                    "La actividad alcanzó su capacidad máxima"
                )

        participacion = Participacion(
            id,
            voluntario_id,
            actividad_id,
            horas
        )

        self.part_repo.add(participacion)

    def get_all_participaciones(self):

        result = []

        for p in self.part_repo.get_all():
            voluntario = self.vol_repo.get_by_id(p.voluntario_id)
            actividad = self.act_repo.get_by_id(p.actividad_id)

            result.append(
                ParticipacionViewDTO(
                    p.id,
                    voluntario.nombre if voluntario else "N/A",
                    actividad.nombre if actividad else "N/A",
                    p.horas
                )
            )

        return result

    # ----------- REPORTES -----------

    def horas_por_voluntario(self, voluntario_id):
        if not self.vol_repo.exists(voluntario_id):
            raise ValueError("El voluntario no existe")

        total = 0

        for p in self.part_repo.get_all():

            if p.voluntario_id == voluntario_id:
                total += p.horas

        return total

    def voluntario_mas_horas(self):

        acumulado = {}

        for p in self.part_repo.get_all():

            if p.voluntario_id not in acumulado:
                acumulado[p.voluntario_id] = 0

            acumulado[p.voluntario_id] += p.horas

        if not acumulado:
            return None

        mejor_id = max(acumulado, key=acumulado.get)

        voluntario = self.vol_repo.get_by_id(mejor_id)

        return voluntario.nombre, acumulado[mejor_id]

    def cantidad_voluntarios_activos(self):

        total = 0

        for voluntario in self.vol_repo.get_all():

            if voluntario.estado.lower() == "activo":
                total += 1

        return total

    def actividad_mas_participacion(self):

        conteo = {}

        for participacion in self.part_repo.get_all():

            if participacion.actividad_id not in conteo:
                conteo[participacion.actividad_id] = 0

            conteo[participacion.actividad_id] += 1

        if not conteo:
            return None

        mejor_id = max(conteo, key=conteo.get)

        actividad = self.act_repo.get_by_id(mejor_id)

        return actividad.nombre, conteo[mejor_id]