import unittest

from src.atracador import Atracador
from src.atraco import Atraco
from src.berlin import Berlin
from src.nairobi import Nairobi
from src.profesor import Profesor
from src.rio import Rio
from src.tokio import Tokio


class TestCasaDePapel(unittest.TestCase):
    def setUp(self):
        self.atraco = Atraco("Fábrica de Moneda y Timbre", "Imprimir billetes")
        self.banda = [
            Profesor("Sergio Marquina", "Profesor"),
            Berlin("Andrés de Fonollosa", "Berlín"),
            Tokio("Silene Oliveira", "Tokio"),
            Rio("Aníbal Cortés", "Río"),
            Nairobi("Ágata Jiménez", "Nairobi"),
        ]

    def test_atracador_es_abstracta(self):
        with self.assertRaises(TypeError):
            Atracador("A", "B")

    def test_herencia(self):
        for a in self.banda:
            self.assertIsInstance(a, Atracador)

    def test_polimorfismo_ejecutar(self):
        resultados = {a.ejecutar() for a in self.banda}
        self.assertEqual(len(resultados), 5)

    def test_participa_en_bidireccional(self):
        tokio = self.banda[2]
        tokio.participar_en(self.atraco)
        self.assertIs(tokio.atraco, self.atraco)
        self.assertIn(tokio, self.atraco.participantes)
        self.atraco.agregar_participante(tokio)
        self.assertEqual(len(self.atraco.participantes), 1)

    def test_estres_con_limite(self):
        t = self.banda[2]
        t.aumentar_estres(500)
        self.assertEqual(t.nivel_estres, 100)
        with self.assertRaises(ValueError):
            t.aumentar_estres(-1)

    def test_iniciar_sin_participantes(self):
        with self.assertRaises(ValueError):
            self.atraco.iniciar()

    def test_profesor_planifica_actualiza_plan(self):
        profesor = self.banda[0]
        profesor.participar_en(self.atraco)
        profesor.planificar()
        self.assertEqual(self.atraco.plan, profesor.plan_maestro)

    def test_planificar_sin_atraco(self):
        with self.assertRaises(ValueError):
            self.banda[1].planificar()

    def test_validacion_niveles(self):
        with self.assertRaises(ValueError):
            Rio("Aníbal", "Río", nivel_hacking=11)


if __name__ == "__main__":
    unittest.main()