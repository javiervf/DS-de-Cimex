import openpyxl
from pathlib import Path
from collections import defaultdict


def clean(str):
    str = str.replace("á", "a")
    str = str.replace("é", "e")
    str = str.replace("í", "i")
    str = str.replace("ó", "o")
    str = str.replace("ú", "u")

    str = str.rsplit(",")[0]
    str = str.rsplit(" ")[0]

    return str


class ObtenerInformacion:
    xlsx_file = Path('Rutas_Outbound.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)

    Ruta_ = wb_obj['Ruta']

    row = Ruta_.max_row
    # columnaFecha = 1
    COLUMNA_NUMERO_TRANSPORTE = 2
    COLUMNA_ORIGEN = 4
    COLUMNA_DESTINO = 5
    COLUMNA_DISTANCIA = 13
    COLUMNA_TONELADAS = 12

    ciudadesCambiadas = {}
    sonMismaCiudad = {}

    rutas = {}

    DISTANCIA_MINIMA_MISMA_CIUDAD = 60

    @staticmethod
    def crearDicionarios(self):
        for i in range(2, self.row + 1):
            if (self.Ruta_.cell(i, self.COLUMNA_ORIGEN).value not in [0, '0', "", " ", None, "(blank)"] and
                    self.Ruta_.cell(i, self.COLUMNA_DESTINO).value not in ['a recogido', "", " ", None, "(blank)"] and
                    "Radial" not in self.Ruta_.cell(i, self.COLUMNA_DESTINO).value):

                origen = clean(self.Ruta_.cell(i, self.COLUMNA_ORIGEN).value)
                destino = clean(self.Ruta_.cell(i, self.COLUMNA_DESTINO).value)

                if self.Ruta_.cell(i, self.COLUMNA_DISTANCIA).value < self.DISTANCIA_MINIMA_MISMA_CIUDAD:

                    if origen not in self.sonMismaCiudad:
                        self.sonMismaCiudad[origen] = [destino]
                    elif destino not in self.sonMismaCiudad[origen]:
                        self.sonMismaCiudad[origen].append(destino)

                    if destino not in self.sonMismaCiudad:
                        self.sonMismaCiudad[destino] = [origen]
                    elif origen not in self.sonMismaCiudad[destino]:
                        self.sonMismaCiudad[destino].append(origen)

                ruta = [self.Ruta_.cell(i, self.COLUMNA_NUMERO_TRANSPORTE).value,
                        destino,
                        float(self.Ruta_.cell(i, self.COLUMNA_TONELADAS)),
                        float(self.Ruta_.cell(i, self.COLUMNA_DISTANCIA))]

                if origen not in self.rutas:
                    self.rutas[origen] = [ruta]
                elif destino not in self.sonMismaCiudad[origen]:
                    self.rutas[origen].append(ruta)

    @staticmethod
    def idkYet(self):
        for i in range(0, len(arregloRuta) - 1):
            siguiente = False
            if i == len(arregloRuta):
                break
            while not siguiente:
                destino = str(arregloRuta[i][2])
                sep = ','
                arregloRuta[i][2] = destino.split(sep, 1)[0]
                for j in range(0, len(aCorregir) - 1):
                    if arregloRuta[i][1] == aCorregir[i][1]:
                        arregloRuta[i][1] = aCorregir[i][2]
                        break
                if 'Radial' in destino:
                    arregloRuta.remove(arregloRuta[i])
                    continue
                if 'D.F.' in destino or 'DF' in destino or 'CDMX' in destino or 'Zona' in destino:
                    arregloRuta[i][2] = 'México'
                if arregloRuta[i][1] == arregloRuta[i][2]:
                    arregloRuta.remove(arregloRuta[i])
                    continue
                if i == len(arregloRuta):
                    break
                siguiente = True

        rutaFinal = []
        guardar = True

        for i in range(0, len(arregloRuta) - 1):
            guardar = True
            origen = arregloRuta[i][1]
            destino = arregloRuta[i][2]
            for j in range(i + 1, len(arregloRuta) - 1):
                if arregloRuta[j][1] == origen:
                    if arregloRuta[j][2] == destino:
                        guardar = False
            if guardar:
                rutaFinal.append(arregloRuta[i])

        print(rutaFinal)

        origenes = []

# for i in range(0, len(rutaFinal) - 1):
# 	guardar = True
# origen = arregloRuta[i][1]
# for j in range(i + 1, len(arregloRuta) - 1):
# 	guardar = True
# 	if arregloRuta[j][1] == origen:
# 		guardar = False
# if origenes is not None:
# 	for k in range(0, len(origenes) - 1):
# 		if arregloRuta[i][1] == origenes[k]:
# 			guardar = False
# if guardar:
# 	origenes.append(arregloRuta[i][1])
#
# destinos = []
#
# for i in range(0, len(rutaFinal) - 1):
# 	guardar = True
# 	destino = arregloRuta[i][2]
# 	for j in range(i + 1, len(arregloRuta) - 1):
# 		guardar = True
# 		if arregloRuta[j][2] == destino:
# 			guardar = False
# 	if destinos is not None:
# 		for k in range(0, len(destinos) - 1):
# 			if arregloRuta[i][2] == destinos[k]:
# 				guardar = False
# 	if guardar:
# 		destinos.append(arregloRuta[i][1])
#
# print(origenes)
# print(destinos)
