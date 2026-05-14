import json
import os

from src.ucr.ac.cr.model.actividad import Actividad

class ActividadRepository:

    def __init__(self, filename="actividades.json"):
        self.filename = filename
        self._actividades = []
        self._by_id = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            a = Actividad.from_dict(item)
            self._actividades.append(a)
            self._by_id[a.id] = a

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([a.to_dict() for a in self._actividades], file, indent=4)

    def add(self, actividad):
        if actividad.id in self._by_id:
            raise ValueError("actividad ya existe")

        self._actividades.append(actividad)
        self._by_id[actividad.id] = actividad
        self._save()

    def get_all(self):
        return list(self._actividades)

    def get_by_id(self, id):
        return self._by_id.get(id)

    def exists(self, id):
        return id in self._by_id