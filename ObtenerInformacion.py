import openpyxl
from pathlib import Path
from collections import defaultdict
from Node import Node
from copy import deepcopy


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
	rutasHelper = {}
	rutasNodos = {}

	arbol = []

	DISTANCIA_MINIMA_MISMA_CIUDAD = 60
	DISTANCIA_MAXIMA_CIRCUITO = 4600 # la ruta con distancia maxima es 2292km
	DEPTH_MAXIMA_CIRCUITO = 4

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
					self.rutasHelper[origen] = [destino]
					self.rutasNodos[origen] = [node]
				elif destino not in self.rutasHelper.get(origen, [None, None]) and destino != origen:
					self.rutas[origen].append(ruta)
					self.rutasHelper[origen].append(destino)
					self.rutasNodos[origen].append(node)

		for k,v in self.sonMismaCiudad.items():
			print(k + ": [" + ", ".join(v) + "]")

		#Node.buildTree(Node, self.rutasNodos, self.DISTANCIA_MAXIMA_CIRCUITO)
		#for k in self.rutasNodos.keys():
		#	print(k)
		#	for v in self.rutasNodos[k]:
		#		Node.printTree(Node, v, 1)

	@staticmethod
	def CrearArbolRutas(self, nodoPapa, esInicio = False):
		if esInicio:
			for k in self.rutas.keys():
				n = Node()
				n.ciudadFinal = k
				self.arbol.append(n)
				self.CrearArbolRutas(self, self.arbol[-1])
			return

		lista = []
		if nodoPapa.ciudadDestino is not None and nodoPapa.ciudadDestino != "":
			try:
				lista = self.rutasNodos[nodoPapa.ciudadDestino]
			except:
				lista = self.rutasNodos.get(self.sonMismaCiudad.get(nodoPapa.ciudadDestino, [None])[0], [])
		else:
			lista = self.rutasNodos[nodoPapa.ciudadFinal]

		for ruta in lista:
			ruta_ = deepcopy(ruta)
			nodoPapa.hijos.append(ruta_)
			ruta_.nodoPadre = nodoPapa
			ruta_.ciudadesPrevias.append(nodoPapa.ciudadDestino)
			ruta_.depth = nodoPapa.depth + 1
			ruta_.distanciaEfectiva = nodoPapa.distanciaEfectiva + ruta.distanciaRuta
			ruta_.ciudadFinal = nodoPapa.ciudadFinal

			# print("p: " + str(nodoPapa.depth) + "; h: " + str(ruta_.depth))
			# print("p:" + str(nodoPapa.distanciaEfectiva) + "; h:" + str(ruta_.distanciaEfectiva))
			# print(ruta_.ciudadDestino + "; " + ' '.join(self.sonMismaCiudad.get(ruta_.ciudadDestino, ['None'])) + "==" + ruta_.ciudadFinal)
			if ruta_.ciudadDestino in ruta_.ciudadesPrevias or any(i in self.sonMismaCiudad.get(ruta_.ciudadDestino, [None]) for i in ruta_.ciudadesPrevias):
				del nodoPapa.hijos[-1]
				return
			if ruta_.ciudadDestino == ruta_.ciudadFinal or ruta_.ciudadFinal in self.sonMismaCiudad.get(ruta_.ciudadDestino, [None]):
				if ruta_.ciudadFinal in self.sonMismaCiudad.get(ruta_.ciudadDestino, [None]):
					ruta.ciudadDestino += "(" + ruta_.ciudadFinal + ")"
				return
			if ruta_.depth > self.DEPTH_MAXIMA_CIRCUITO or ruta_.distanciaEfectiva > self.DISTANCIA_MAXIMA_CIRCUITO:
				del nodoPapa.hijos[-1]
				return

			self.CrearArbolRutas(self, ruta_)

		if nodoPapa is not None and len(nodoPapa.hijos) == 0 and nodoPapa.nodoPadre is not None:
			nodoPapa.nodoPadre.hijos.remove(nodoPapa)

	@staticmethod
	def LimpiarArbolRutas(self, nodo, esInicio = False):
		if esInicio:
			for k in self.rutas.keys():
				self.LimpiarArbolRutas(self, self.arbol[-1])
			return

		if nodo is None:
			return

		for hijo in nodo.hijos:
			self.LimpiarArbolRutas(self, hijo)

		if len(nodo.hijos) == 0 and not (nodo.ciudadDestino == nodo.ciudadFinal or nodo.ciudadFinal in self.sonMismaCiudad.get(nodo.ciudadDestino, [None])):
			nodo.nodoPadre.hijos.remove(nodo)
			del nodo
			return

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
