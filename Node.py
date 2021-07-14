class Node:
    # ciudadOrigen = ""
    # ciudadDestino = ""
    # toneladas = 0
    # viajes = 0
    # distanciaRuta = 0
    #
    # depth = 0
    #
    # toneladasEfectivas = 0
    # viajesEfectivos = 0
    # distanciaEfectiva = 0
    # ciudadFinal = ""
    # ciudadPapa = None
    # hijos = []

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
        self.nodoPadre = None



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
        try:
            print(n*"\t" + who.ciudadOrigen + " -> " + who.ciudadDestino)
        except:
            print(n * "\t" + who.ciudadFinal)
        if (n > 3):
            #print( "wit")
            #return
            pass
        for hijo in who.hijos:
            self.printTree(self, hijo, n+1)
