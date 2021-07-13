import openpyxl
from pathlib import Path
from collections import defaultdict
from ObtenerInformacion import ObtenerInformacion
from Node import Node

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
    n = ObtenerInformacion
    ObtenerInformacion.CrearDiccionarios(n)
    #ObtenerInformacion.ImprimirRutas(n, "Torreon")
    #ObtenerInformacion.ImprimirRutasKilometro(n)
    ObtenerInformacion.CrearArbolRutas(n, None, True)

    for k in ObtenerInformacion.arbol:
        #print(k.ciudadOrigen)
        Node.printTree(Node, k, 0)

    print("end")





