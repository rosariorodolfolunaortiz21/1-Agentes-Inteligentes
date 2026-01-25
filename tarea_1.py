#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea_1.py
------------
Revisa el archivo README.md con las instrucciones de la tarea.
"""
__author__ = 'Rosario Rodolfo Luna Ortiz'

from entornos_o import Entorno, Agente
import random


# ============================
# Entorno NueveCuartos
# ============================
class NueveCuartos(Entorno):
    def __init__(self):
        super().__init__()

        # Dimensiones
        self.pisos = 3
        self.cuartos_por_piso = 3

        # Posición inicial (piso, cuarto)
        self.posicion = (1, 1)

        # Estado de los cuartos
        self.estado = {}
        for piso in range(1, 4):
            for cuarto in range(1, 4):
                self.estado[(piso, cuarto)] = "sucio"

        # Función de desempeño y costo
        self.desempeno = 0
        self.costo_total = 0

        # Costos de acciones
        self.costos = {
            "subir": 7,
            "bajar": 5,
            "ir_Derecha": 3,
            "ir_Izquierda": 3,
            "limpiar": 1,
            "nada": 0
        }

    def accion_legal(self, accion):
        piso, cuarto = self.posicion

        if accion in ["limpiar", "nada"]:
            return True

        if accion == "ir_Derecha":
            return cuarto < 3

        if accion == "ir_Izquierda":
            return cuarto > 1

        if accion == "subir":
            return piso < 3 and cuarto == 3

        if accion == "bajar":
            return piso > 1 and cuarto == 1

        return False

    def costo_accion(self, accion):
        return self.costos.get(accion, 0)

    def transicion(self, accion):
        if not self.accion_legal(accion):
            return

        # Manejo de costos
        costo = self.costo_accion(accion)
        self.costo_total += costo
        self.desempeno -= costo

        piso, cuarto = self.posicion

        if accion == "limpiar":
            if self.estado[(piso, cuarto)] == "sucio":
                self.estado[(piso, cuarto)] = "limpio"
                self.desempeno += 10  # recompensa por limpiar

        elif accion == "ir_Derecha":
            self.posicion = (piso, cuarto + 1)

        elif accion == "ir_Izquierda":
            self.posicion = (piso, cuarto - 1)

        elif accion == "subir":
            self.posicion = (piso + 1, cuarto)

        elif accion == "bajar":
            self.posicion = (piso - 1, cuarto)

        elif accion == "nada":
            pass

    def percepcion(self):
        piso, cuarto = self.posicion
        return self.posicion, self.estado[(piso, cuarto)]


# ============================
# Agente Aleatorio
# ============================
class AgenteAleatorio(Agente):
    def __init__(self):
        self.acciones = [
            "ir_Derecha", "ir_Izquierda",
            "subir", "bajar",
            "limpiar", "nada"
        ]

    def programa(self, percepcion):
        return random.choice(self.acciones)


# ============================
# Simulación simple
# ============================
def simular_agente(entorno, agente, pasos=50):
    print("\n--- INICIO SIMULACIÓN ---\n")

    for i in range(pasos):
        p = entorno.percepcion()
        accion = agente.programa(p)

        if entorno.accion_legal(accion):
            entorno.transicion(accion)

        print(f"Paso {i}")
        print(f"  Posición: {entorno.posicion}")
        print(f"  Estado actual: {entorno.estado[entorno.posicion]}")
        print(f"  Acción: {accion}")
        print(f"  Costo total: {entorno.costo_total}")
        print(f"  Desempeño: {entorno.desempeno}")
        print("-" * 30)

    print("\n--- FIN SIMULACIÓN ---")
    print(f"Costo total final: {entorno.costo_total}")
    print(f"Desempeño final: {entorno.desempeno}")


# ============================
# Prueba principal
# ============================
if __name__ == "__main__":
    entorno = NueveCuartos()
    agente = AgenteAleatorio()

    simular_agente(entorno, agente, pasos=30)
