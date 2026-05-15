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

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not telefono.strip():
            raise ValueError("El teléfono no puede estar vacío")

        if not telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números")

        if tipo.lower() not in ["permanente", "ocasional"]:
            raise ValueError("Tipo inválido")

        if estado.lower() not in ["activo", "inactivo"]:
            raise ValueError("Estado inválido")

        for voluntario in self.vol_repo.get_all():

            if voluntario.id == id:
                raise ValueError("Ya existe un voluntario con ese ID")

            if voluntario.telefono == telefono:
                raise ValueError("Ya existe un voluntario con ese teléfono")

        voluntario = Voluntario(id, nombre, telefono, tipo, estado)
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

        if not self.vol_repo.exists(voluntario_id):
            raise ValueError("El voluntario no existe")

        if not self.act_repo.exists(actividad_id):
            raise ValueError("La actividad no existe")

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        if horas > 24:
            raise ValueError("Las horas no pueden ser mayores a 24")

        for participacion in self.part_repo.get_all():
            if (participacion.voluntario_id == voluntario_id
                    and participacion.actividad_id == actividad_id
            ):
                raise ValueError("El voluntario ya participa en esta actividad")

        actividad = self.act_repo.get_by_id(actividad_id)

        if actividad.capacidad_maxima > 0:

            participantes_actuales = 0

            for participacion in self.part_repo.get_all():

                if participacion.actividad_id == actividad_id:
                    participantes_actuales += 1

            if participantes_actuales >= actividad.capacidad_maxima:
                raise ValueError("La actividad alcanzó su capacidad máxima")

        participacion = Participacion(
            id, voluntario_id, actividad_id, horas
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
                acumulado[p.voluntario_id]= 0

            acumulado[p.voluntario_id] += p.horas

        if not acumulado:
            return  None

        mejor_id = max(acumulado, key = acumulado.get)

        voluntario = self.vol_repo.get_by_id(mejor_id)

        return voluntario.nombre, acumulado[mejor_id]

    def cantidad_voluntarios_activos(self):

        total = 0

        for v in self.vol_repo.get_all():
            if v.estado.lower() == "activo":
                total += 1

        return  total


    def actividad_mas_participacion(self):

        conteo = {}

        for p in self.part_repo.get_all():
            if p.actividad_id not in conteo:
                conteo[p.actividad_id] = 0

            conteo[p.actividad_id] += 1

        if not conteo:
            return None

        mejor_id = max(conteo, key = conteo.get)

        actividad = self.act_repo.get_by_id(mejor_id)

        return actividad.nombre, conteo[mejor_id]