import json
import os
from src.ucr.ac.cr.model.voluntario import Voluntario

class VoluntarioRepository:

    def __init__(self, filename="voluntarios.json"):
        self.filename = filename
        self._voluntarios = []
        self._by_id = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            v = Voluntario.from_dict(item)
            self._voluntarios.append(v)
            self._by_id[v.id] = v

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([v.to_dict() for v in self._voluntarios], file, indent=4)

    def add(self, voluntario):
        if voluntario.id in self._by_id:
            raise ValueError("El voluntario ya existe")

        self._voluntarios.append(voluntario)
        self._by_id[voluntario.id] = voluntario
        self._save()

    def get_all(self):
        return list(self._voluntarios)

    def get_by_id(self, id):
        return self._by_id.get(id)

    def exists(self, id):
        return id in self._by_id