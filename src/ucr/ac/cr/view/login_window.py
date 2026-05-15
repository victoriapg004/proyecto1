import tkinter as tk
from tkinter import messagebox

from src.ucr.ac.cr.view.main_window import MainWindow


class LoginWindow:

    def __init__(self, root, controller):

        self.root = root
        self.controller = controller

        self.intentos = 3

        self.root.title("Login")
        self.root.geometry("400x500")
        self.root.configure(bg="#fff5f5")
        self.root.resizable(False, False)

        self._build()

    def _build(self):

        container = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="groove",
            padx=20,
            pady=20
        )

        container.pack(
            padx=40,
            pady=40,
            fill="both",
            expand=True
        )

        tk.Label(
            container,
            text="Sistema de Voluntariado",
            font=("Arial", 18, "bold"),
            fg="#b30000",
            bg="white"
        ).pack(pady=10)

        tk.Label(
            container,
            text="Usuario",
            font=("Arial", 12),
            bg="white"
        ).pack(pady=(10, 5))

        self.entry_user = tk.Entry(container, width=30)

        self.entry_user.pack(pady=5)

        tk.Label(
            container,
            text="Contraseña",
            font=("Arial", 12),
            bg="white"
        ).pack(pady=(10, 5))

        self.entry_password = tk.Entry(
            container,
            width=30,
            show="*"
        )

        self.entry_password.pack(pady=5)

        tk.Label(
            container,
            text="Usuario: admin | Contraseña: 1234",
            font=("Arial", 9),
            bg="white",
            fg="gray"
        ).pack(pady=5)

        tk.Button(
            container,
            text="Iniciar sesión",
            font=("Arial", 12, "bold"),
            bg="#cc0000",
            fg="white",
            width=18,
            command=self.login
        ).pack(pady=20)

    def login(self):

        user = self.entry_user.get()
        password = self.entry_password.get()

        # usuario simple para proyecto

        if user == "admin" and password == "1234":

            messagebox.showinfo(
                "Bienvenido",
                "Bienvenido al Sistema de Voluntariado de la Cruz Roja"
            )

            self.root.destroy()

            new_root = tk.Tk()

            MainWindow(new_root, self.controller)

            new_root.mainloop()

        else:

            self.intentos -= 1

            messagebox.showerror(
                "Credenciales incorrectas",
                f"Usuario o contraseña inválidos.\n"
                f"Intentos restantes: {self.intentos}"
            )

            if self.intentos == 0:

                messagebox.showerror(
                    "Acceso bloqueado",
                    "Ha superado el número máximo de intentos."
                )

                self.root.destroy()