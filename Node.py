class Node:
    def __init__(self, destino = "", toneladas = 0, distancia = 0, origen = None, ciudadFinal = None, ciudadPapa = None):
        self.ciudadOrigen = ""
        self.ciudadDestino = ""
        self.toneladas = 0
        self.viajes = 0
        self.distanciaRuta = 0

        self.depth = 0

        self.toneladasEfectivas = 0
        self.viajesEfectivos = 0
        self.distanciaEfectiva = 0
        self.ciudadFinal = ""
        self.ciudadPapa = None
        self.hijos = []
        self.ciudadesPrevias = []
        self.nodoPadre = None



        self.ciudadOrigen = origen
        self.ciudadDestino = destino
        self.toneladas = toneladas
        self.ciudadFinal = ciudadFinal
        self.ciudadPapa = ciudadPapa
        self.distanciaRuta = distancia


    @staticmethod
    def printTree(self, who, n):
        try:
            print(n*"\t" + who.ciudadOrigen + " -> " + who.ciudadDestino)
        except:
            print(n * "\t" + who.ciudadFinal)

        for hijo in who.hijos:
            self.printTree(self, hijo, n+1)
