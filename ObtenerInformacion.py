import openpyxl
from pathlib import Path
from collections import defaultdict
from Node import Node


def clean(returnString):
	if any(element in returnString for element in ['D.F.', 'DF', 'CDMX', 'Zona']):
		returnString = 'México'

	returnString = returnString.replace("á", "a")
	returnString = returnString.replace("é", "e")
	returnString = returnString.replace("í", "i")
	returnString = returnString.replace("ó", "o")
	returnString = returnString.replace("ú", "u")

	returnString = returnString.rsplit(",")[0]
	#returnString = returnString.rsplit(" ")[0]

	return returnString


class ObtenerInformacion:
	def __init__(self):
		pass

	xlsx_file = Path('Rutas_Outbound.xlsx')
	wb_obj = openpyxl.load_workbook(xlsx_file)

	Ruta_ = wb_obj['Ruta']

	row = Ruta_.max_row
	# columnaFecha = 1
	COLUMNA_NUMERO_TRANSPORTE = 2
	COLUMNA_ORIGEN = 4
	COLUMNA_DESTINO = 5
	COLUMNA_DISTANCIA = 16
	COLUMNA_TONELADAS = 12

	ciudadesCambiadas = {}
	sonMismaCiudad = {}

	rutas = {}
	rutasNodos = {}

	arbol = {}

	DISTANCIA_MINIMA_MISMA_CIUDAD = 60
	DISTANCIA_MAXIMA_CIRCUITO = 4600 # la ruta con distancia maxima es 2292km

	@staticmethod
	def CrearDiccionarios(self):
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
						float(self.Ruta_.cell(i, self.COLUMNA_TONELADAS).value),
						float(self.Ruta_.cell(i, self.COLUMNA_DISTANCIA).value)]

				node = Node(destino, float(self.Ruta_.cell(i, self.COLUMNA_TONELADAS).value), float(self.Ruta_.cell(i, self.COLUMNA_DISTANCIA).value), origen, origen)

				if origen not in self.rutas:
					self.rutas[origen] = [ruta]
					self.rutasNodos[origen] = [node]
				elif destino not in self.rutas.get(origen, [None, None]) and self.sonMismaCiudad.get(destino, [None])[0] not in self.rutas.get(origen, [None, None]) and destino != origen:
					self.rutas[origen].append(ruta)
					self.rutasNodos[origen].append(node)

				 #if v[1] not in printed and self.sonMismaCiudad.get(v[1], [None])[0] not in printed and self.sonMismaCiudad.get(v[1], [None])[0] != k:


		for k in self.rutasNodos.keys():
			print(k)
			for v in self.rutasNodos[k]:
				Node.printTree(Node, v, 1)

	@staticmethod
	def CrearArbolRutas(self):
		for k in self.rutas.keys():
			printed = [[k, 0]]
			for v in self.rutas[k]:
				if v[1] not in printed and self.sonMismaCiudad.get(v[1], [None])[0] not in printed and self.sonMismaCiudad.get(v[1], [None])[0] != k:
					printed.append([v[1], v[3]])
					printed[0][0] = max(printed[0][0], v[3])
			self.arbol[k] = printed[1:]


	@staticmethod
	def ImprimirRutasKilometro(self):
		for k in self.rutas.keys():
			print(k)
			printed = []
			for v in self.rutas[k]:
				#print("A = " + k + " ; B =" + self.sonMismaCiudad.get(v[1], ["as"])[0] + " ; C = ", self.sonMismaCiudad.get(v[1], ["as"])[0] != k)
				if v[1] not in printed and self.sonMismaCiudad.get(v[1], [None])[0] not in printed and self.sonMismaCiudad.get(v[1], [None])[0] != k:
					print("\t" + str(v[1]) + ": " + str(v[3]) + "km")
					printed.append(v[1])

	@staticmethod
	def ImprimirRutas(self):
		print(self.rutas)

	@staticmethod
	def ImprimirRutas(self, ciudad):
		print(self.rutas[ciudad])
