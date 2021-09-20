import os
import sys

def encabezado():
	os.system("cls")
	print("\t\t\tJuan Pablo Malagón Morales\nDeyanira López Méndez\nHéctor Gerardo Carvajal Sánchez")
	print("\t\tRaíces de un polinomio: Teorema de Sturm\n\n")

#Regresa el valor del polinomio P evaluado en c
def evaluar(p, c):
	n = 0.0

	for x in range(len(p)):
		n += p[x] * (c**x)

	return n

#Determina si c es raíz del último polinomio de la cadena
def es_raiz(c):
	for x in range(len(cadena)):
		n = evaluar(cadena[x], c)

		if n == 0:
			return True

	return False

def ingreso_datos():
	encabezado()
	print("Ingreso de datos: \n\n")
	print("Ingrese el grado máximo del polinomio libre de cuadrados: ")

	grado = int(input())

	global cadena

	for x in range(grado + 1):
		encabezado()
		print("Ingreso de datos: \n\n")
		print(f"Ingrese el coeficiente de grado {x}: ")
		cadena[0].append(float(input()))

	encabezado()
	print("Ingreso de datos: \n\n")
	print("Introduzca el elemento \"a\" del intervale (a,b): ")
	global a
	a = float(input())

	encabezado()
	print("Ingreso de datos: \n\n")
	print("Introduzca el elemento \"b\" del intervale (a,b): ")
	global b
	b = float(input())

	if es_raiz(a):
		print(f"{a} es raíz de P")
		sys.exit(1)
	elif es_raiz(b):
		print(f"{b} es raíz de P")
		sys.exit(1)

	encabezado()
	print("Ingreso de datos: \n\n")
	print("Introduzca el margen de error: ")
	global epsi
	epsi = float(input())

def residuo(p0, p1, k):
	grado = len(p0) - len(p1)
	coef = p0[len(p0) - 1] / p1[len(p1) - 1]

	temp = [[], []]

	for x in range(len(p0)):
		temp[0].append(0)
		temp[1].append(0)

	for x in range(len(p1)):
		temp[0][x + grado] = coef * p1[x]

	for x in range(len(p0)):
		temp[1][x] = p0[x] - temp[0][x]

	while temp[1][len(temp[1]) - 1] == 0:
		temp[1].pop()

	if len(temp[1]) >= len(p1):
		residuo(temp[1], p1, k)
	elif len(temp[1]) != 0:
		global cadena
		cadena.append([])

		for x in range(len(temp[1])):
			cadena[k].append(-temp[1][x])

	if evaluar(cadena[k], a) == 0:
		print(f"{a} es raíz de P{k}")
		sys.exit(1)
	elif evaluar(cadena[k], b) == 0:
		print(f"{b} es raíz de P{k}")
		sys.exit(1)

def imprimir_cadena():
	encabezado()

	print(f"\tIntervalo ({a}, {b})\t\tMargen de error = {epsi}\n\n")

	for x in range(len(cadena)):
		print(f"\nP{x} =", end = " ")

		for y in range(len(cadena[x])):
			if cadena[x][len(cadena[x]) - y - 1] > 0:
				print(f"+{cadena[x][len(cadena[x]) - y - 1]}x^{len(cadena[x]) - y - 1}", end = "")
			elif cadena[x][len(cadena[x]) - y - 1] < 0:
				print(f"{cadena[x][len(cadena[x]) - y - 1]}x^{len(cadena[x]) - y - 1}", end = "")

def cambio_signo(c):
	cambios = 0

	for x in range(len(cadena)):
		n = evaluar(cadena[x], c)

		if x == 0:
			if n > 0:
				signo = 1
			else:
				signo = -1
		elif (n > 0 and signo == -1) or (n < 0 and signo == 1):
			cambios += 1

			if n > 0:
				signo = 1
			else:
				signo = -1

	return cambios

def obten_raiz(p, a, b):
	c = (a + b) / 2
	n = evaluar(p, c)
	global itermax
	itermax += 1

	if n == 0 or itermax == 10:
		print(f"Hay una raiz en {c} dentro del márgen de error\n")
	elif n * evaluar(p, a) < 0:
		obten_raiz(p, a, c)
	else:
		obten_raiz(p, c, b)

def raices(a, b):
	j = cambio_signo(a) - cambio_signo(b)

	c = (b + a) / 2

	if j != 0:
		if j == 1:
			global itermax
			itermax = 0
			obten_raiz(cadena[0], a, b)
		elif b - a < 2 * epsi:
			print(f"Hay {j} raíces entre {c - epsi} y {c + epsi}\n")
		else:
			while es_raiz(c):
				c += 0.01

			raices(a, c)
			raices(c, b)

#Declaramos las variables globales
cadena = [[]]
a = None
b = None
epsi = None

ingreso_datos()

#Generamos P1
cadena.append([])

for x in range(1, len(cadena[0])):
	cadena[1].append(float(int(x) * int(cadena[0][x])))

if es_raiz(a):
	print(f"{a} es raíz de P[1]")
	sys.exit(1)
elif es_raiz(b):
	print(f"{b} es raíz de P[1]")
	sys.exit(1)


#Generar el resto de la cadena
k = len(cadena)

while len(cadena[k - 1]) > 1:
	residuo(cadena[k-2], cadena[k-1], k)
	k = len(cadena)

imprimir_cadena()

#Encontrar raíces
print("\n\n\n\tRaices:\n")
itermax = None
raices(a, b)
