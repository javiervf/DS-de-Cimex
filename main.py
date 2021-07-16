from ObtenerInformacion import ObtenerInformacion
from Node import Node

if __name__ == '__main__':
    print("start\n")

    n = ObtenerInformacion
    #ObtenerInformacion.Cosita(n)
    ObtenerInformacion.CreacionMismaCiudad2(n)
    ObtenerInformacion.CrearDiccionarios(n)
    ObtenerInformacion.CrearArbolRutas(n, None, True)
    ObtenerInformacion.LimpiarArbolRutas(n, None, True)
    ObtenerInformacion.Backpropagate(n, None, True)

    for k in ObtenerInformacion.arbol:
        Node.printTree(Node, k, 0)


    print("\nend")





