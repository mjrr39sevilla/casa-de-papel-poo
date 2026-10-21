from src.atracador import Atracador


class Rio(Atracador):
    def __init__(self, nombre: str, alias: str, nivel_hacking: int = 9):
        super().__init__(nombre, alias)
        self._nivel_hacking = self._validar_nivel(nivel_hacking, "nivel_hacking")

    @property
    def nivel_hacking(self) -> int:
        return self._nivel_hacking

    def hackear(self) -> str:
        return f"{self._alias} hackea el sistema (nivel {self._nivel_hacking}/10)."

    def ejecutar(self) -> str:
        return self.hackear()