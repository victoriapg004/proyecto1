import tkinter as tk
from tkinter import messagebox

class ActividadFrame(tk.Frame):

    def __init__(self, parent, controller, query_frame):
        super().__init__(parent, bg="#f2f2f2")

        self.controller = controller
        self.query_frame = query_frame

        self._build()

    def _build(self):

        container = tk.Frame(self, bg="white", bd=2, relief="groove", padx=20, pady=20)
        container.pack(padx=30, pady=20, fill="x")

        tk.Label(container, text="Registrar nueva actividad", font=("Arial", 18, "bold"), fg="#b30000", bg="white").grid(
            row=0, column=0, columnspan=2, pady=(0, 20)
        )

        labels = [
            "ID de la actividad:",
            "Nombre:",
            "Fecha (YYYY/MM/DD):",
            "Ubicación:",
            "Capacidad máxima:",
        ]

        for i, texto in enumerate(labels):
            tk.Label(container, text=texto, font=("Arial", 12), bg="white").grid(
                row=i + 1, column=0, padx=10, pady=10, sticky="e")

        self.entry_id = tk.Entry(container, width=35)
        self.entry_nombre = tk.Entry(container, width=35)
        self.entry_fecha = tk.Entry(container, width=35)
        self.entry_ubicacion = tk.Entry(container, width=35)
        self.entry_capacidad = tk.Entry(container, width=35)

        self.entry_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)
        self.entry_fecha.grid(row=3, column=1, padx=10, pady=10)
        self.entry_ubicacion.grid(row=4, column=1, padx=10, pady=10)
        self.entry_capacidad.grid(row=5, column=1, padx=10, pady=10)

        button_frame = tk.Frame(container, bg="white")
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        tk.Button(button_frame, text="Registrar actividad", font=("Arial", 12, "bold"), width=20, bg="#cc0000", fg="white", command=self.register_activity).pack(
            side="left", padx=10)

    def register_activity(self):

        try:

            id_ = self.entry_id.get()
            nombre = self.entry_nombre.get()
            fecha = self.entry_fecha.get()
            ubicacion = self.entry_ubicacion.get()
            capacidad = self.entry_capacidad.get()

            self.controller.add_actividad(
                id_,nombre,fecha,ubicacion,capacidad
            )

            messagebox.showinfo("Éxito", "Actividad registrada correctamente")

            self.clear_entries()

        except Exception as e:

            messagebox.showerror("Error", str(e))

    def clear_entries(self):

        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_ubicacion.delete(0, tk.END)
        self.entry_capacidad.delete(0, tk.END)