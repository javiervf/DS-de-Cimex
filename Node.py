class Node:
    def __init__(self, destino = "", toneladas = 0, distancia = 0, origen = None, viajes = 0, ciudadPapa = None):
        self.ciudadOrigen = ""
        self.ciudadDestino = ""
        self.toneladas = 0
        self.viajes = 0
        self.distanciaRuta = 0

        self.depth = 0

        self.toneladasMax = 0
        self.viajesMax = 0
        self.distanciaEfectiva = 0
        self.ciudadFinal = ""
        self.ciudadPapa = None
        self.hijos = []
        self.ciudadesPrevias = []
        self.nodoPadre = None



        self.ciudadOrigen = origen
        self.ciudadDestino = destino
        self.toneladas = toneladas
        self.ciudadPapa = ciudadPapa
        self.distanciaRuta = distancia
        self.viajes = viajes


    @staticmethod
    def printTree(self, who, n):
        try:
            print(n*"\t" + who.ciudadOrigen + " -> " + who.ciudadDestino + ": " + str(round(who.toneladasMax, 2)) + "ton. " + str(round(who.viajesMax, 2)) + " viaj.")
        except:
            if who.toneladasMax == 999999999:
                who.toneladasMax = 0
                who.viajesMax = 0
            print(n * "\t" + who.ciudadFinal + ": " + str(round(who.toneladasMax, 2)) + "ton. " + str(round(who.viajesMax, 2)) + " viaj.")

        for hijo in who.hijos:
            self.printTree(self, hijo, n+1)
