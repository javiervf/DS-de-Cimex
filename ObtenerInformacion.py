import openpyxl
from pathlib import Path
from collections import defaultdict

xlsx_file = Path('Rutas_Outbound.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)

Ruta_ = wb_obj['Ruta']

###################### Ruta

row = Ruta_.max_row
# columnaFecha = 1
columnaNumeroTransporte = 2
columnaOrigen = 4
columnaDestino = 5
columnaDistancia = 16
# columnaToneladas = 12

arregloRuta = []
aCorregir = []

# run for loop which will read all records from sheet one by one
for i in range(2, row + 1):
	if Ruta_.cell(i, columnaOrigen).value != '0':
		if Ruta_.cell(i, columnaOrigen).value != 0:
			if Ruta_.cell(i, columnaDistancia).value < 60:
				aCorregir.append([Ruta_.cell(i, columnaNumeroTransporte).value, Ruta_.cell(i, columnaOrigen).value,
									Ruta_.cell(i, columnaDestino).value, Ruta_.cell(i, columnaDistancia)])
				arregloRuta.append([Ruta_.cell(i, columnaNumeroTransporte).value, Ruta_.cell(i, columnaOrigen).value,
									Ruta_.cell(i, columnaDestino).value, Ruta_.cell(i, columnaDistancia).value])
			else:
				arregloRuta.append([Ruta_.cell(i, columnaNumeroTransporte).value, Ruta_.cell(i, columnaOrigen).value,
								Ruta_.cell(i, columnaDestino).value, Ruta_.cell(i, columnaDistancia).value])

for i in range(0, len(arregloRuta) - 1):
	siguiente = False
	if i == len(arregloRuta):
		break
	while not siguiente:
		destino = str(arregloRuta[i][2])
		sep = ','
		arregloRuta[i][2] = destino.split(sep, 1)[0]
		for j in range(0, len(aCorregir) - 1):
			if arregloRuta[i][1] == aCorregir[j][1]:
				arregloRuta[i][1] = aCorregir[j][2]
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

#############################