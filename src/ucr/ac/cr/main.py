import tkinter as tk

from src.ucr.ac.cr.model.voluntario_repository import VoluntarioRepository
from src.ucr.ac.cr.model.actividad_repository import ActividadRepository
from src.ucr.ac.cr.model.participacion_repository import ParticipacionRepository
from src.ucr.ac.cr.service.voluntariado_service import VoluntariadoService
from src.ucr.ac.cr.controller.voluntariado_controller import VoluntariadoController
from src.ucr.ac.cr.view.main_window import MainWindow


def main():

    vol_repo = VoluntarioRepository()
    act_repo = ActividadRepository()
    part_repo = ParticipacionRepository()

    service = VoluntariadoService(vol_repo, act_repo, part_repo)
    controller = VoluntariadoController(service)

    root = tk.Tk()
    MainWindow(root, controller)
    root.mainloop()
#jijijaja
if __name__ == "__main__":
    main()