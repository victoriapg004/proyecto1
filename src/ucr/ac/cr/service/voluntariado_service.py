from src.ucr.ac.cr.model.voluntario import Voluntario
from src.ucr.ac.cr.model.actividad import Actividad
from src.ucr.ac.cr.model.participacion import Participacion
from src.ucr.ac.cr.model.dto import ParticipacionViewDTO


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

        voluntario = Voluntario(id, nombre, telefono, tipo, estado)
        self.vol_repo.add(voluntario)

        print(self.vol_repo.get_all())

    def get_voluntarios(self):
        return self.vol_repo.get_all()

    # ----------- ACTIVIDAD -----------

    def register_actividad(self, id, nombre, fecha, tipo, ubicacion):

        if not id.strip():
            raise ValueError("El ID no puede estar vacío")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        actividad = Actividad(id, nombre, fecha, tipo, ubicacion)
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

        participacion = Participacion(id, voluntario_id, actividad_id, horas)
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

    # ----------- PROCESO (IMPORTANTE PARA NOTA) -----------

    def horas_por_voluntario(self, voluntario_id):

        if not self.vol_repo.exists(voluntario_id):
            raise ValueError("El voluntario no existe")

        total = 0

        for p in self.part_repo.get_all():
            if p.voluntario_id == voluntario_id:
                total += p.horas

        return total