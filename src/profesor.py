from src.atracador import Atracador


class Profesor(Atracador):
    def __init__(self, nombre: str, alias: str,
                 plan_maestro: str = "Imprimir billetes sin violencia"):
        super().__init__(nombre, alias)
        self._plan_maestro = self._validar_texto(plan_maestro, "plan_maestro")

    @property
    def plan_maestro(self) -> str:
        return self._plan_maestro

    def coordinar(self) -> str:
        return (f"{self._alias} coordina a la banda según el plan maestro: "
                f"{self._plan_maestro}.")

    def planificar(self) -> str:
        super().planificar()
        self._atraco.actualizar_plan(self._plan_maestro)
        return f"{self._alias} fija el plan maestro del atraco: {self._plan_maestro}."

    def ejecutar(self) -> str:
        return self.coordinar()