import tkinter as tk
from tkinter import messagebox

class ReportFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self._build()


    def _build(self):

        title = tk.Label(
            self,
            text="REPORTES DEL SISTEMA",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        #Horas por voluntariado
        tk.Label(
            self,
            text="ID del voluntario:"
        ).pack()

        self.entry_id = tk.Entry(self, width=30)
        self.entry_id.pack(pady=5)

        tk.Button(
            self,
            text="Consultar horas",
            bg="#cc0000",
            fg="white",
            activebackground="#990000",
            activeforeground="white",
            command=self.show_horas_voluntario
        ).pack(pady=10)

        #Voluntariado destacado
        tk.Button(
            self,
            text="Voluntario con más horas",
            bg="#cc0000",
            fg="white",
            activebackground="#990000",
            activeforeground="white",
            command=self.show_mejor_voluntario
        ).pack(pady=10)

        #Activos
        tk.Button(
            self,
            text="Cantidad de voluntarios activos",
            bg="#cc0000",
            fg="white",
            activebackground="#990000",
            activeforeground="white",
            command=self.show_activos
        ).pack(pady=10)

        #Actividad destacada
        tk.Button(
            self,
            text="Actividad con más participación",
            command=self.show_actividad,
            bg = "#cc0000",
            fg = "white",
            activebackground = "#990000",
            activeforeground = "white"
        ).pack(pady=10)

    # ---------------- REPORTES ----------------

    def show_horas_voluntario(self):

        try:
            voluntario_id = self.entry_id.get()

            total = self.controller.get_horas_voluntario(voluntario_id)

            messagebox.showinfo(
                "Reporte",
                f"Horas totales: {total}"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_mejor_voluntario(self):

        data = self.controller.get_voluntario_mas_horas()

        if data:
            nombre, horas = data

            messagebox.showinfo(
                "Reporte",
                f"Voluntario destacado:\n{nombre}\nHoras: {horas}"
            )

    def show_activos(self):

        total = self.controller.get_cantidad_activos()

        messagebox.showinfo(
            "Reporte",
            f"Voluntarios activos: {total}"
        )

    def show_actividad(self):

        data = self.controller.get_actividad_mas_participacion()

        if data:
            nombre, cantidad = data

            messagebox.showinfo(
                "Reporte",
                f"Actividad destacada:\n{nombre}\nParticipaciones: {cantidad}"
            )