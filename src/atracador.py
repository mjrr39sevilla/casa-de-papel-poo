"""Clase abstracta Atracador (clase padre del diagrama)."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.atraco import Atraco


class Atracador(ABC):
    """ABSTRACCIÓN: define lo común a todos los atracadores."""

    ESTRES_MAX = 100

    def __init__(self, nombre: str, alias: str, edad: Optional[int] = None):
        # ENCAPSULACIÓN: atributos privados (-) con acceso controlado.
        self._nombre = self._validar_texto(nombre, "nombre")
        self._alias = self._validar_texto(alias, "alias")
        if edad is not None and (not isinstance(edad, int) or edad < 0):
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = edad
        self._nivel_estres = 0
        self._atraco: Optional["Atraco"] = None

    # ---------- utilidades ----------
    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not valor or not valor.strip():
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_nivel(valor: int, campo: str) -> int:
        if not isinstance(valor, int) or not 0 <= valor <= 10:
            raise ValueError(f"'{campo}' debe ser un entero entre 0 y 10.")
        return valor

    # ---------- propiedades (solo lectura) ----------
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> Optional[int]:
        return self._edad

    @property
    def nivel_estres(self) -> int:
        return self._nivel_estres

    @property
    def atraco(self) -> Optional["Atraco"]:
        return self._atraco

    # ---------- métodos del diagrama ----------
    def obtener_alias(self) -> str:
        return self._alias

    def aumentar_estres(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("La cantidad de estrés debe ser positiva.")
        self._nivel_estres = min(self.ESTRES_MAX, self._nivel_estres + cantidad)

    def participar_en(self, atraco: "Atraco") -> None:
        """Relación 'participa en' (Atracador -> Atraco)."""
        if self._atraco is atraco:
            return
        self._atraco = atraco
        atraco.agregar_participante(self)

    def planificar(self) -> str:
        if self._atraco is None:
            raise ValueError(f"{self._alias} no participa en ningún atraco.")
        return (f"{self._alias} planifica su parte del atraco "
                f"'{self._atraco.nombre}'.")

    @abstractmethod
    def ejecutar(self) -> str:
        """Cada subclase ejecuta su parte a su manera (polimorfismo)."""

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._alias})"