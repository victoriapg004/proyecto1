import tkinter as tk
from tkinter import messagebox


class ParticipacionFrame(tk.Frame):

    def __init__(self, parent, controller, query_frame):
        super().__init__(parent)
        self.controller = controller
        self.query_frame = query_frame
        self._build()

    def _build(self):
        tk.Label(self, text="ID de la participación:", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="ID del voluntario:", font=("Arial", 12)).grid(
            row=1, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="ID de la actividad:", font=("Arial", 12)).grid(
            row=2, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="Horas:", font=("Arial", 12)).grid(
            row=3, column=0, padx=10, pady=10, sticky="e"
        )

        # Entradas
        self.entry_id = tk.Entry(self, width=35)
        self.entry_voluntario = tk.Entry(self, width=35)
        self.entry_actividad = tk.Entry(self, width=35)
        self.entry_horas = tk.Entry(self, width=35)

        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_voluntario.grid(row=1, column=1, padx=10, pady=10)
        self.entry_actividad.grid(row=2, column=1, padx=10, pady=10)
        self.entry_horas.grid(row=3, column=1, padx=10, pady=10)

        # Botón registrar
        tk.Button(
            self,
            text="Registrar participación",
            font=("Arial", 12, "bold"),
            width=20,
            command=self.register_participacion
        ).grid(row=4, column=0, columnspan=2, pady=15)

        # Botón listar
        tk.Button(
            self,
            text="Lista de participaciones",
            font=("Arial", 12),
            width=20,
            command=self.query_frame.show_participaciones
        ).grid(row=5, column=0, columnspan=2, pady=5)

    def register_participacion(self):
        try:
            id_ = self.entry_id.get()
            voluntario_id = self.entry_voluntario.get()
            actividad_id = self.entry_actividad.get()
            horas = int(self.entry_horas.get())  # importante convertir a int

            self.controller.add_participacion(
                id_, voluntario_id, actividad_id, horas
            )

            messagebox.showinfo("Éxito", "Participación registrada correctamente")
            self.clear_entries()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_voluntario.delete(0, tk.END)
        self.entry_actividad.delete(0, tk.END)
        self.entry_horas.delete(0, tk.END)