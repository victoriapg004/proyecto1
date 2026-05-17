import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import ttk

from src.ucr.ac.cr.view.voluntario_frame import VoluntarioFrame
from src.ucr.ac.cr.view.actividad_frame import ActividadFrame
from src.ucr.ac.cr.view.participacion_frame import ParticipacionFrame
from src.ucr.ac.cr.view.query_frame import QueryFrame
from src.ucr.ac.cr.view.report_frame import ReportFrame


class MainWindow:


    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.configure(bg = "#fff5f5" )

        self.root.title("SISTEMA DE VOLUNTARIADO DE LA CRUZ ROJA")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        self._build()

    def _build(self):
        ruta_logo = os.path.join(
            os.path.dirname(__file__),
            "..",
            "images",
            "cruzRoja.jpg"
        )

        imagen = Image.open(ruta_logo)

        imagen = imagen.resize((50, 50), Image.LANCZOS)

        self.logo = ImageTk.PhotoImage(imagen)

        logo_label = tk.Label(
            self.root,
            image=self.logo,
            bg="#fff5f5"
        )

        logo_label.image = self.logo

        logo_label.pack(pady=10)

        title = tk.Label(self.root,text="SISTEMA DE VOLUNTARIADO DE LA CRUZ ROJA",
            font=("Arial", 24, "bold"),
            fg = "#b30000",
            bg = "#fff5f5"
        )
        title.pack(pady=10)

        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "TNotebook.Tab",
            font = ("Arial", 10, "bold"),
            padding=[12, 6]
        )

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=(0,10))

        query_frame = QueryFrame(notebook, self.controller)
        voluntario_frame = VoluntarioFrame(notebook, self.controller, query_frame)
        actividad_frame = ActividadFrame(notebook, self.controller, query_frame)
        participacion_frame = ParticipacionFrame(notebook, self.controller, query_frame)
        report_frame = ReportFrame(notebook, self.controller)

        #query_frame.set_notebook(notebook)

        notebook.add(voluntario_frame, text="voluntarios")
        notebook.add(actividad_frame, text="actividades")
        notebook.add(participacion_frame, text="participaciones")
        notebook.add(query_frame, text="consultas")
        notebook.add(report_frame, text="reportes")