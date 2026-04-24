class VoluntariadoController:

    def __init__(self, service):
        self.service = service

    # ----------- REGISTROS -----------

    def add_voluntario(self, id, nombre, telefono, tipo, estado):
        self.service.register_voluntario(id, nombre, telefono, tipo, estado)

    def add_actividad(self, id, nombre, fecha, tipo, ubicacion):
        self.service.register_actividad(id, nombre, fecha, tipo, ubicacion)

    def add_participacion(self, id, voluntario_id, actividad_id, horas):
        self.service.register_participacion(id, voluntario_id, actividad_id, horas)

    # ----------- CONSULTAS -----------

    def get_voluntarios(self):
        return self.service.get_voluntarios()

    def get_actividades(self):
        return self.service.get_actividades()

    def get_participaciones(self):
        return self.service.get_all_participaciones()