"""Clase Atraco: el golpe en el que participan los atracadores."""
from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:  # evita importación circular en tiempo de ejecución
    from src.atracador import Atracador


class Atraco:
    def __init__(self, nombre: str, objetivo: str, botin: float = 0.0,
                 plan: str = "Sin plan definido"):
        self._nombre = self._validar_texto(nombre, "nombre")
        self._objetivo = self._validar_texto(objetivo, "objetivo")
        if botin < 0:
            raise ValueError("El botín no puede ser negativo.")
        self._botin = botin
        self._plan = self._validar_texto(plan, "plan")
        self._participantes: List["Atracador"] = []
        self._en_curso = False

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not valor or not valor.strip():
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")
        return valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def objetivo(self) -> str:
        return self._objetivo

    @property
    def botin(self) -> float:
        return self._botin

    @property
    def plan(self) -> str:
        return self._plan

    @property
    def en_curso(self) -> bool:
        return self._en_curso

    @property
    def participantes(self) -> List["Atracador"]:
        return list(self._participantes)  # copia: la lista interna queda protegida

    def agregar_participante(self, atracador: "Atracador") -> None:
        if atracador in self._participantes:
            return
        self._participantes.append(atracador)
        atracador.participar_en(self)  # mantiene la relación en ambos sentidos

    def iniciar(self) -> List[str]:
        """Inicia el atraco: cada atracador ejecuta su parte (polimorfismo)."""
        if not self._participantes:
            raise ValueError("No se puede iniciar un atraco sin participantes.")
        self._en_curso = True
        return [a.ejecutar() for a in self._participantes]

    def actualizar_plan(self, nuevo_plan: str) -> None:
        self._plan = self._validar_texto(nuevo_plan, "plan")

    def __str__(self) -> str:
        return f"Atraco('{self._nombre}': {self._objetivo})"