import tkinter as tk
from tkinter import messagebox


class VoluntarioFrame(tk.Frame):

    def __init__(self, parent, controller, query_frame):
        super().__init__(parent, bg="#f2f2f2")

        self.controller = controller
        self.query_frame = query_frame

        self._build()

    def _build(self):

        container = tk.Frame(self,bg="white",bd=2,relief="groove",padx=20,pady=20)

        container.pack(padx=30,pady=20,fill="x")

        tk.Label(container,text="Registrar nuevo voluntario",font=("Arial", 18, "bold"),fg="#b30000",bg="white").grid(
            row=0,column=0,columnspan=2,pady=(0, 20))

        labels = [
            "ID del voluntario:",
            "Nombre:",
            "Teléfono:",
            "Tipo:",
            "Estado:"
        ]

        for i, texto in enumerate(labels):

            tk.Label(container,text=texto,font=("Arial", 12),bg="white").grid(
                row=i + 1,column=0,padx=10,pady=10,sticky="e"
            )

        self.entry_id = tk.Entry(container, width=35)
        self.entry_nombre = tk.Entry(container, width=35)
        self.entry_telefono = tk.Entry(container, width=35)

        self.entry_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)

        self.tipo_var = tk.StringVar(value="permanente")
        self.estado_var = tk.StringVar(value="activo")

        tipo_frame = tk.Frame(container, bg="white")

        tipo_frame.grid(
            row=4,column=1,padx=10,pady=10,sticky="w")

        tk.Radiobutton(tipo_frame,text="Permanente",variable=self.tipo_var,value="permanente",bg="white").pack(side="left", padx=5)

        tk.Radiobutton(tipo_frame,text="Ocasional",variable=self.tipo_var,value="ocasional",bg="white").pack(side="left", padx=5)

        estado_frame = tk.Frame(container, bg="white")

        estado_frame.grid(
            row=5,column=1,padx=10,pady=10, sticky="w")

        tk.Radiobutton(estado_frame,text="Activo",variable=self.estado_var,value="activo",bg="white").pack(side="left", padx=5)

        tk.Radiobutton(estado_frame,text="Inactivo",variable=self.estado_var,value="inactivo",bg="white").pack(side="left", padx=5)

        button_frame = tk.Frame(container,bg="white")

        button_frame.grid(
            row=6,column=0,columnspan=2,pady=20)

        tk.Button(button_frame,text="Registrar voluntario",font=("Arial", 12, "bold"),width=20,bg="#cc0000",fg="white",command=self.register_voluntario).pack(
            side="left",padx=10)

    def register_voluntario(self):

        try:

            id_ = self.entry_id.get()
            nombre = self.entry_nombre.get()
            telefono = self.entry_telefono.get()
            tipo = self.tipo_var.get()
            estado = self.estado_var.get()

            self.controller.add_voluntario(
                id_,nombre,telefono,tipo,estado
            )

            messagebox.showinfo(
                "Éxito","Voluntario registrado correctamente"
            )

            self.clear_entries()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def clear_entries(self):

        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

        self.tipo_var.set("permanente")
        self.estado_var.set("activo")