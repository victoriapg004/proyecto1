import tkinter as tk
from tkinter import ttk, messagebox


class ReportFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f2f2f2")

        self.controller = controller
        self._build()

    def _build(self):

        container = tk.Frame(self, bg="white", bd=2, relief="groove", padx=20, pady=20)
        container.pack(padx=30, pady=20, fill="both", expand=True)

        tk.Label(container,text="Reportes del sistema",font=("Arial", 20, "bold"),fg="#b30000",bg="white").pack(pady=(0, 20))

        id_frame = tk.Frame(container, bg="white")
        id_frame.pack(pady=10)

        tk.Label(id_frame,text="ID del voluntario:",font=("Arial", 12),bg="white").pack(side="left", padx=5)

        self.entry_id = tk.Entry(id_frame, width=25, font=("Arial", 11))
        self.entry_id.pack(side="left", padx=5)

        button_frame = tk.Frame(container, bg="white")
        button_frame.pack(pady=15)

        tk.Button(button_frame,text="Consultar horas",font=("Arial", 11, "bold"),width=18,bg="#cc0000",fg="white",command=self.show_horas_voluntario).grid(
            row=0, column=0, padx=10, pady=10)

        tk.Button(button_frame,text="Voluntario destacado",font=("Arial", 11, "bold"),width=22,bg="#cc0000",fg="white",command=self.show_mejor_voluntario).grid(
            row=0, column=1, padx=10, pady=10)

        tk.Button(button_frame,text="Voluntarios activos",font=("Arial", 11, "bold"),width=22,bg="#cc0000",fg="white",command=self.show_activos).grid(
            row=1, column=0, padx=10, pady=10)

        tk.Button(button_frame,text="Actividad destacada",font=("Arial", 11, "bold"),width=22,bg="#cc0000",fg="white",command=self.show_actividad).grid(
            row=1, column=1, padx=10, pady=10)

        self.tree = ttk.Treeview(container, show="headings")
        self.tree.pack(fill="both", expand=True, pady=20)


    def clear_table(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

    def setup_columns(self, columns):

        self.tree["columns"] = columns

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor="center")

    # ---------------- HORAS VOLUNTARIO ----------------

    def show_horas_voluntario(self):

        try:

            voluntario_id = self.entry_id.get()

            total = self.controller.get_horas_voluntario(voluntario_id)

            self.clear_table()

            self.setup_columns(("ID Voluntario", "Horas Totales"))

            self.tree.insert("", "end", values=(voluntario_id, total))

        except Exception as e:

            messagebox.showerror("Error", str(e))

    # ---------------- VOLUNTARIO DESTACADO ----------------

    def show_mejor_voluntario(self):

        data = self.controller.get_voluntario_mas_horas()

        if data:

            nombre, horas = data

            self.clear_table()

            self.setup_columns(("Voluntario", "Horas"))

            self.tree.insert("", "end",
                             values=(nombre, horas))

    # ---------------- ACTIVOS ----------------

    def show_activos(self):

        total = self.controller.get_cantidad_activos()

        self.clear_table()

        self.setup_columns(("Reporte", "Cantidad"))

        self.tree.insert("", "end",
                         values=("Voluntarios activos", total))

    # ---------------- ACTIVIDAD DESTACADA ----------------

    def show_actividad(self):

        data = self.controller.get_actividad_mas_participacion()

        if data:

            nombre, cantidad = data

            self.clear_table()

            self.setup_columns(("Actividad", "Participaciones"))

            self.tree.insert("", "end",
                             values=(nombre, cantidad))
