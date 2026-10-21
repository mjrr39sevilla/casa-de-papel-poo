from src.atraco import Atraco
from src.berlin import Berlin
from src.nairobi import Nairobi
from src.profesor import Profesor
from src.rio import Rio
from src.tokio import Tokio


def main() -> None:
    # --- Objetos ---
    profesor = Profesor("Sergio Marquina", "Profesor")
    tokio = Tokio("Silene Oliveira", "Tokio")
    berlin = Berlin("Andrés de Fonollosa", "Berlín")
    rio = Rio("Aníbal Cortés", "Río")
    nairobi = Nairobi("Ágata Jiménez", "Nairobi")
    atraco = Atraco("Fábrica de Moneda y Timbre", "Imprimir billetes")

    # --- Relación "participa en" ---
    banda = [profesor, berlin, tokio, rio, nairobi]
    for atracador in banda:
        atracador.participar_en(atraco)

    print(f"{atraco} con {len(atraco.participantes)} participantes\n")

    # --- Planificar ---
    print(profesor.planificar())
    print(f"Plan del atraco: {atraco.plan}\n")

    # --- Polimorfismo: metodo, comportamiento distinto ---
    for linea in atraco.iniciar():
        print(" ->", linea)

    # --- Métodos subclase ---
    print()
    print(tokio.narrar())
    print(berlin.liderar())

    # --- Encapsulación ---
    tokio.aumentar_estres(130)
    print(f"\nEstrés de {tokio.obtener_alias()}: {tokio.nivel_estres}")
    atraco.actualizar_plan("Plan B: salir por el túnel")
    print(f"Plan actualizado: {atraco.plan}")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
