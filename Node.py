class Node:
    ciudadOrigen = ""
    ciudadDestino = ""
    toneladas = 0
    viajes = 0
    distanciaRuta = 0

    toneladasEfectivas = 0
    viajesEfectivos = 0
    ciudadFinal = ""
    ciudadPapa = None
    hijos = []

    def __init__(self, destino, toneladas, distancia, origen = None, ciudadFinal = None, ciudadPapa = None):
        self.ciudadOrigen = origen
        self.ciudadDestino = destino
        self.toneladas = toneladas
        self.ciudadFinal = ciudadFinal
        self.ciudadPapa = ciudadPapa
        self.distanciaRuta = distancia


    def backPropogate(self):
        pass

    def crearHijos(self):
        pass

    def esFinal(self):
        pass

    @staticmethod
    def printTree(self, who, n):
        print(n*"\t" + who.ciudadOrigen + " -> " + who.ciudadDestino)
        for hijo in who.hijos:
            self.printTree(hijo, n+1)
