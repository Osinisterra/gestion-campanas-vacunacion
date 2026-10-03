import os

from nicegui import ui


class Application:
    def configure(self) -> None:
        ui.page("/")(self.show_home)

    def show_home(self) -> None:
        ui.label("Gestión de campañas de vacunación").classes("text-2xl")
        ui.label("Base del proyecto · Universidad Santiago de Cali")

    def run(self) -> None:
        self.configure()
        ui.run(
            host="0.0.0.0",
            port=int(os.environ.get("PORT", "8080")),
            title="Gestión de campañas de vacunación",
            show=False,
            reload=False,
            uvicorn_logging_level="info",
            language="es",
        )
