from src.atracador import Atracador


class Tokio(Atracador):
    def __init__(self, nombre: str, alias: str, impulsividad: int = 8):
        super().__init__(nombre, alias)
        self._impulsividad = self._validar_nivel(impulsividad, "impulsividad")

    @property
    def impulsividad(self) -> int:
        return self._impulsividad

    def narrar(self) -> str:
        return f"{self._alias} narra la historia del atraco."

    def ejecutar(self) -> str:
        return (f"{self._alias} actúa por impulso "
                f"(impulsividad {self._impulsividad}/10).")