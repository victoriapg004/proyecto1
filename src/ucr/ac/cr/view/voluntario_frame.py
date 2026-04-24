import tkinter as tk
from tkinter import messagebox


class VoluntarioFrame(tk.Frame):

    def __init__(self, parent, controller, query_frame):
        super().__init__(parent)
        self.controller = controller
        self.query_frame = query_frame
        self._build()

    def _build(self):
        tk.Label(self, text="ID del voluntario:", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="Nombre:", font=("Arial", 12)).grid(
            row=1, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="Teléfono:", font=("Arial", 12)).grid(
            row=2, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="Tipo(permanente/ocasional):", font=("Arial", 12)).grid(
            row=3, column=0, padx=10, pady=10, sticky="e"
        )
        tk.Label(self, text="Estado(activo/inactivo):", font=("Arial", 12)).grid(
            row=4, column=0, padx=10, pady=10, sticky="e"
        )

        # Entradas
        self.entry_id = tk.Entry(self, width=35)
        self.entry_nombre = tk.Entry(self, width=35)
        self.entry_telefono = tk.Entry(self, width=35)
        self.entry_tipo = tk.Entry(self, width=35)
        self.entry_estado = tk.Entry(self, width=35)

        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)
        self.entry_telefono.grid(row=2, column=1, padx=10, pady=10)
        self.entry_tipo.grid(row=3, column=1, padx=10, pady=10)
        self.entry_estado.grid(row=4, column=1, padx=10, pady=10)

        # Botón registrar
        tk.Button(
            self,
            text="Registrar voluntario",
            font=("Arial", 12, "bold"),
            width=20,
            command=self.register_voluntario
        ).grid(row=5, column=0, columnspan=2, pady=15)

        # Botón listar
        tk.Button(
            self,
            text="Lista de voluntarios",
            font=("Arial", 12),
            width=20,
            command=self.query_frame.show_voluntarios
        ).grid(row=6, column=0, columnspan=2, pady=5)

    def register_voluntario(self):
        try:
            id_ = self.entry_id.get()
            nombre = self.entry_nombre.get()
            telefono = self.entry_telefono.get()
            tipo = self.entry_tipo.get()
            estado = self.entry_estado.get()

            self.controller.add_voluntario(id_, nombre, telefono, tipo, estado)

            messagebox.showinfo("Éxito", "Voluntario registrado correctamente")
            self.clear_entries()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_estado.delete(0, tk.END)