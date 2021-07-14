from ObtenerInformacion import ObtenerInformacion
from Node import Node

if __name__ == '__main__':
    print("start\n")

    n = ObtenerInformacion
    ObtenerInformacion.CrearDiccionarios(n)
    ObtenerInformacion.CrearArbolRutas(n, None, True)
    ObtenerInformacion.LimpiarArbolRutas(n, None, True)

    for k in ObtenerInformacion.arbol:
        Node.printTree(Node, k, 0)


    print("\nend")





