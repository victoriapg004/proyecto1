class Actividad:

    def __init__(self, id, nombre, fecha, tipo, ubicacion):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.ubicacion = ubicacion

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)