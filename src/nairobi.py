from src.atracador import Atracador


class Nairobi(Atracador):
    def __init__(self, nombre: str, alias: str, falsificacion: int = 9):
        super().__init__(nombre, alias)
        self._falsificacion = self._validar_nivel(falsificacion, "falsificacion")

    @property
    def falsificacion(self) -> int:
        return self._falsificacion

    def falsificar(self) -> str:
        return (f"{self._alias} falsifica los billetes "
                f"(habilidad {self._falsificacion}/10).")

    def ejecutar(self) -> str:
        return self.falsificar()