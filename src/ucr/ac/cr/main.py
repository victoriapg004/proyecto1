import tkinter as tk

from src.ucr.ac.cr.repository.voluntario_repository import VoluntarioRepository
from src.ucr.ac.cr.repository.actividad_repository import ActividadRepository
from src.ucr.ac.cr.repository.participacion_repository import ParticipacionRepository

from src.ucr.ac.cr.service.voluntariado_service import VoluntariadoService
from src.ucr.ac.cr.controller.voluntariado_controller import VoluntariadoController

from src.ucr.ac.cr.view.login_window import LoginWindow


def main():

    vol_repo = VoluntarioRepository()
    act_repo = ActividadRepository()
    part_repo = ParticipacionRepository()

    service = VoluntariadoService(
        vol_repo,
        act_repo,
        part_repo
    )

    controller = VoluntariadoController(service)

    root = tk.Tk()

    LoginWindow(root, controller)

    root.mainloop()


if __name__ == "__main__":
    main()

    #ULTIMA ACTUALIZACION 16 YULIANA