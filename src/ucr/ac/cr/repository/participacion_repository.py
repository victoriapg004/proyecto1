import json
import os
from src.ucr.ac.cr.model.participacion import Participacion

class ParticipacionRepository:

    def __init__(self, filename="participaciones.json"):
        self.filename = filename
        self._participaciones = []
        self._by_id = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            p = Participacion.from_dict(item)
            self._participaciones.append(p)
            self._by_id[p.id] = p

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([p.to_dict() for p in self._participaciones], file, indent=4)

    def add(self, participacion):
        if participacion.id in self._by_id:
            raise ValueError("participacion ya existe")

        self._participaciones.append(participacion)
        self._by_id[participacion.id] = participacion
        self._save()

    def get_all(self):
        return list(self._participaciones)

    def get_by_id(self, id):
        return self._by_id.get(id)

    def exists(self, id):
        return id in self._by_id