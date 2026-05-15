class Actividad:

    def __init__(self, id, nombre, fecha, ubicacion,capacidad_maxima):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
          return cls(**data)