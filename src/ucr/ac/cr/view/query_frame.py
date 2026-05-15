import tkinter as tk
from tkinter import ttk


class QueryFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f2f2f2")

        self.controller = controller
        self._build()

    def _build(self):

        container = tk.Frame(self, bg="white", bd=2, relief="groove", padx=20, pady=20)

        container.pack(padx=30, pady=20, fill="both", expand=True)

        tk.Label(container, text="Consultas del sistema", font=("Arial", 20, "bold"), fg="#b30000", bg="white").pack(
            pady=(0, 20))

        button_frame = tk.Frame(container, bg="white")

        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Ver voluntarios", font=("Arial", 12, "bold"), width=20, bg="#cc0000", fg="white", command=self.show_voluntarios).pack(
            side="left", padx=10)

        tk.Button(button_frame, text="Ver actividades", font=("Arial", 12, "bold"), width=20, bg="#cc0000", fg="white", command=self.show_actividades).pack(
            side="left", padx=10)

        tk.Button(button_frame, text="Ver participaciones", font=("Arial", 12, "bold"), width=20, bg="#cc0000", fg="white", command=self.show_participaciones).pack(
            side="left", padx=10)

        self.tree = ttk.Treeview(container)

        self.tree.pack(fill="both", expand=True, pady=20)

    # ---------------- VOLUNTARIOS ----------------

    def show_voluntarios(self):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = (
            "ID",
            "Nombre",
            "Teléfono",
            "Tipo",
            "Estado"
        )

        self.tree["show"] = "headings"

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for voluntario in self.controller.get_voluntarios():

            self.tree.insert("", "end",
                             values=(voluntario.id, voluntario.nombre, voluntario.telefono, voluntario.tipo, voluntario.estado))

    # ---------------- ACTIVIDADES ----------------

    def show_actividades(self):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = (
            "ID",
            "Nombre",
            "Fecha",
            "Ubicación",
            "Cupos disponibles"
        )

        self.tree["show"] = "headings"

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140)

        actividades = self.controller.get_actividades()
        participaciones = self.controller.get_participaciones()

        for actividad in actividades:

            usados = 0

            for participacion in participaciones:

                if participacion.actividad_nombre == actividad.nombre:
                    usados += 1

            disponibles = actividad.capacidad_maxima - usados

            self.tree.insert(
                "",
                "end",
                values=(
                    actividad.id,
                    actividad.nombre,
                    actividad.fecha,
                    actividad.ubicacion,
                    disponibles
                )
            )
    # ---------------- PARTICIPACIONES ----------------

    def show_participaciones(self):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = (
            "ID",
            "Voluntario",
            "Actividad",
            "Horas"
        )

        self.tree["show"] = "headings"

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180)

        for participacion in self.controller.get_participaciones():

            self.tree.insert("", "end",
                             values=(participacion.id,participacion.voluntario_nombre,participacion.actividad_nombre,participacion.horas))