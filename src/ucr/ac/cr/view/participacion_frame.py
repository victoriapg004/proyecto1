import tkinter as tk
from tkinter import messagebox


class ParticipacionFrame(tk.Frame):

    def __init__(self, parent, controller, query_frame):
        super().__init__(parent, bg="#f2f2f2")

        self.controller = controller
        self.query_frame = query_frame

        self._build()

    def _build(self):

        container = tk.Frame(self,bg="white",bd=2,relief="groove",padx=20,pady=20)

        container.pack(padx=30,pady=20, fill="x")

        tk.Label(container,text="Registrar nueva participación",font=("Arial", 18, "bold"),fg="#b30000",bg="white").grid(
            row=0,column=0,columnspan=2,pady=(0, 20)
        )
        labels = [
            "ID de la participación:",
            "ID del voluntario:",
            "ID de la actividad:",
            "Horas:"
        ]

        for i, texto in enumerate(labels):

            tk.Label(container,text=texto,font=("Arial", 12),bg="white").grid(
                row=i + 1,column=0,padx=10,pady=10,sticky="e"
            )

        self.entry_id = tk.Entry(container, width=35)
        self.entry_voluntario = tk.Entry(container, width=35)
        self.entry_actividad = tk.Entry(container, width=35)
        self.entry_horas = tk.Entry(container, width=35)

        self.entry_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_voluntario.grid(row=2, column=1, padx=10, pady=10)
        self.entry_actividad.grid(row=3, column=1, padx=10, pady=10)
        self.entry_horas.grid(row=4, column=1, padx=10, pady=10)


        button_frame = tk.Frame(container,bg="white")

        button_frame.grid(row=5,column=0,columnspan=2,pady=20)

        tk.Button(button_frame,text="Registrar participación",font=("Arial", 12, "bold"),width=20,bg="#cc0000",fg="white",command=self.register_participacion).pack(
            side="left",padx=10)

    def register_participacion(self):

        try:

            id_ = self.entry_id.get()
            voluntario_id = self.entry_voluntario.get()
            actividad_id = self.entry_actividad.get()

            horas = int(self.entry_horas.get())

            self.controller.add_participacion(id_,voluntario_id,actividad_id,horas)

            messagebox.showinfo( "Éxito", "Participación registrada correctamente")

            self.clear_entries()

        except Exception as e:

            messagebox.showerror("Error", str(e))

    def clear_entries(self):

        self.entry_id.delete(0, tk.END)
        self.entry_voluntario.delete(0, tk.END)
        self.entry_actividad.delete(0, tk.END)
        self.entry_horas.delete(0, tk.END)