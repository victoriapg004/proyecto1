class VoluntariadoController:

    def __init__(self, service):
        self.service = service

    # ----------- REGISTROS -----------

    def add_voluntario(self, id, nombre, telefono, tipo, estado):
        self.service.register_voluntario(id, nombre, telefono, tipo, estado)

    def add_actividad(self, id, nombre, fecha, ubicacion,capacidad_maxima=0):
        self.service.register_actividad(id, nombre, fecha, ubicacion,capacidad_maxima)

    def add_participacion(self, id, voluntario_id, actividad_id, horas):
        self.service.register_participacion(id, voluntario_id, actividad_id, horas)

    # ----------- CONSULTAS -----------

    def get_voluntarios(self):
        return self.service.get_voluntarios()

    def get_voluntario_by_id(self, voluntario_id):
        return self.service.get_voluntario_by_id(voluntario_id)

    def get_actividades(self):
        return self.service.get_actividades()

    def get_participaciones(self):
        return self.service.get_all_participaciones()

    # --------- REPORTES ---------------

    def get_horas_voluntario(self, voluntario_id):
        return self.service.horas_por_voluntario(voluntario_id)

    def get_voluntario_mas_horas(self):
        return self.service.voluntario_mas_horas()

    def get_cantidad_activos(self):
        return self.service.cantidad_voluntarios_activos()

    def get_actividad_mas_participacion(self):
        return self.service.actividad_mas_participacion()