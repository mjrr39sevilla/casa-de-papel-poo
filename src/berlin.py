from src.atracador import Atracador


class Berlin(Atracador):
    def __init__(self, nombre: str, alias: str, liderazgo: int = 9):
        super().__init__(nombre, alias)
        self._liderazgo = self._validar_nivel(liderazgo, "liderazgo")

    @property
    def liderazgo(self) -> int:
        return self._liderazgo

    def liderar(self) -> str:
        return f"{self._alias} lidera al grupo (liderazgo {self._liderazgo}/10)."

    def ejecutar(self) -> str:
        return self.liderar()