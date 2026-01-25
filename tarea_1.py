#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea_1.py
------------
Revisa el archivo README.md con las instrucciones de la tarea.
"""
__author__ = 'Rosario Rodolfo Luna Ortiz'

from entornos_o import Entorno
import random


# Inicio del entorno NueveCuartos
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

        # Función de desempeño
        self.desempeno = 0

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

    def transicion(self, accion):
        if not self.accion_legal(accion):
            return

        # Penaliza por energía
        self.desempeno -= self.costos[accion]

        piso, cuarto = self.posicion

        if accion == "limpiar":
            if self.estado[(piso, cuarto)] == "sucio":
                self.estado[(piso, cuarto)] = "limpio"
                self.desempeno += 10  # premio por limpiar

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
