import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
num1 = 2
num2 = 4
num3 = 3


def multiplicar():
    result = num1 * num2 * num3
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    n=1000
    result = 0
    while n>=1000 and n<=2000:
        if (n%3 == 0) and (n%5 == 0):
            result+=n
            n+= 1
        else:
            n+= 1
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->

def definicionOrtoedro():
    result = {"longitud":obtenerArea(),"volumen":obtenerVolumen()}
    return result


def obtenerArea():
    longitud = 10
    latitud = 6
    altura = 5
    result = 2(longitud*latitud+longitud*altura+latitud*altura)
    return result


def obtenerVolumen():
    longitud = 10
    latitud = 6
    altura = 5
    result = longitud*latitud*altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def __init__(self):
        self.octoedro = {}
    def definicionOrtoedro(self, resultDict):
        self.__resultDict= resultDict
        return resultDict
    def obtenerArea(self, longitud, latitud, altura,result)
        self.__longitud = longitud
        self.__latitud = latitud
        self.__altura = altura
        self.__result = result
        return result
    def obtenerVolumen(self, longitud, latitud,altura, result)
        self.__longitud = longitud
        self.__latitud = latitud
        self.__altura = altura
        self.__result = result
        return result


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/Jason-Maravilla/Parcial.git"
