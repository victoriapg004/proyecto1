import tkinter as tk
from tkinter import ttk

from src.ucr.ac.cr.view.voluntario_frame import VoluntarioFrame
from src.ucr.ac.cr.view.actividad_frame import ActividadFrame
from src.ucr.ac.cr.view.participacion_frame import ParticipacionFrame
from src.ucr.ac.cr.view.query_frame import QueryFrame


class MainWindow:


    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("SISTEMA DE VOLUNTARIADO DE LA CRUZ ROJA")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)

        self._build()

    def _build(self):
        title = tk.Label(
            self.root,
            text="SISTEMA DE VOLUNTARIADO DE LA CRUZ ROJA",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        query_frame = QueryFrame(notebook, self.controller)
        voluntario_frame = VoluntarioFrame(notebook, self.controller, query_frame)
        actividad_frame = ActividadFrame(notebook, self.controller, query_frame)
        participacion_frame = ParticipacionFrame(notebook, self.controller, query_frame)

        query_frame.set_notebook(notebook)

        notebook.add(voluntario_frame, text="voluntarios")
        notebook.add(actividad_frame, text="actividades")
        notebook.add(participacion_frame, text="participaciones")
        notebook.add(query_frame, text="consultas")