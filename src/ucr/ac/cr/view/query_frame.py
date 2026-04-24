import tkinter as tk
from tkinter import ttk


class QueryFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.notebook = None
        self._build()

    def set_notebook(self, notebook):
        self.notebook = notebook

    def _build(self):
        self.tree = ttk.Treeview(self)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------------- VOLUNTARIOS ----------------
    def show_voluntarios(self):
        self._clear()

        self.tree["columns"] = ("ID", "Nombre", "Tipo", "Estado")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        voluntarios = self.controller.get_voluntarios()

        for v in voluntarios:
            self.tree.insert("", "end", values=(v.id, v.nombre, v.tipo, v.estado))

        self._show()

    # ---------------- ACTIVIDADES ----------------
    def show_actividades(self):
        self._clear()

        self.tree["columns"] = ("ID", "Nombre", "Fecha", "Tipo", "Ubicación")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        actividades = self.controller.get_actividades()

        for a in actividades:
            self.tree.insert("", "end", values=(
                a.id, a.nombre, a.fecha, a.tipo, a.ubicacion
            ))

        self._show()

    # ---------------- PARTICIPACIONES ----------------
    def show_participaciones(self):
        self._clear()

        self.tree["columns"] = ("ID", "Voluntario", "Actividad", "Horas")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        participaciones = self.controller.get_participaciones()

        for p in participaciones:
            self.tree.insert("", "end", values=(
                p.id, p.voluntario, p.actividad, p.horas
            ))

        self._show()

    # ---------------- UTILIDADES ----------------
    def _clear(self):
        self.tree.delete(*self.tree.get_children())

    def _show(self):
        if self.notebook:
            self.notebook.select(self)