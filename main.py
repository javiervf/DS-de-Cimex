import openpyxl
from pathlib import Path
from collections import defaultdict

informacion = {}

def leerExcel():
    pass

def iniciarNodos():
    pass

def printNodeInfo():
    pass

def printTreeInfo():
    pass

def crearArbol():
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("start")
    leerExcel()
    iniciarNodos()
    crearArbol()
    print("end")


class Node:
    ciudadOrigen = ""
    ciudadDestino = ""
    toneladas = 0
    viajes = 0

    toneladasEfectivas = 0
    viajesEfectivos = 0
    ciudadFinal = ""
    ciudadPapa = None
    hijos = []

    def backPropogate(self):
        pass

    def crearHijos(self):
        pass

    def esFinal(self):
        pass



