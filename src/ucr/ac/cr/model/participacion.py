class Participacion:

    def __init__(self, id, voluntario_id, actividad_id, horas):
        self.id = id
        self.voluntario_id = voluntario_id
        self.actividad_id = actividad_id
        self.horas = horas

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)