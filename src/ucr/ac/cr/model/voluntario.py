class Voluntario:

    def __init__(self, id, nombre, telefono, tipo, estado):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.tipo = tipo
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "tipo": self.tipo,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.tipo}"