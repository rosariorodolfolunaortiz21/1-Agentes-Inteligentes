#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea_1.py
------------
Revisa el archivo README.md con las instrucciones de la tarea.
"""
__author__ = 'Rosario Rodolfo Luna Ortiz'

# Requiere el modulo entornos_f.py o entornos_o.py
# Usa el modulo doscuartos_f.py para reutilizar código
# Agrega los modulos que requieras de python

from entornos_o import Entorno
import random


# Inicio del entorno NueveCuartos
class NueveCuartos(Entorno):
    def __init__(self):
        # Inicializa el entorno base
        super().__init__()

        # Definición del entorno
        self.pisos = 3
        self.cuartos_por_piso = 3

        # Posición inicial del agente (piso, cuarto)
        # usando índices desde 1 por claridad conceptual
        self.posicion = (1, 1)

        # Estado de los cuartos: limpio o sucio
        self.estado = {}

        for piso in range(1, 4):
            for cuarto in range(1, 4):
                self.estado[(piso, cuarto)] = "sucio"
