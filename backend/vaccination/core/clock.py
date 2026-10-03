from datetime import UTC, datetime


class Clock:
    """Hora UTC del servidor; sustituible por un reloj fijo en pruebas."""

    def now(self) -> datetime:
        return datetime.now(UTC)
