import random

class Persona:

    #Constructor
    def __init__(self, nombre="", edad=0, dni="", sexo="F", peso=0, altura=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    #Métodos set
    def setnombre(self, nombre):
        self.__nombre = nombre
    def getnombre (self):
        return self.__nombre

    def setedad(self,edad):
        self.__edad=edad
    def getedad (self):
        return self.__edad

    def setsexo(self, sexo):
        self.__sexo
    def getsexo (self):
        return self.__sexo

    def setpeso(self, peso):
        self.__peso
    def getpeso (self):
        return self.__peso

    def setaltura(self, altura):
        self.__altura
    def getaltura (self):
        return self.__altura

    #Método para calcular IMC
    def calcularIMC(self, peso, altura):

        imc = peso / (altura**2)

        if imc >= 0 and imc <= 15.99:
            return -1

        elif imc >= 18.50 and imc <= 24.99:
            return 0

        elif imc >= 40.00:
            return 1

    #Método para comprbar que sea mayor de edad
    def esMayordeEdad(self, edad):
        if edad >= 18 :
            return True
        else:
            return False

    #Método para introducir sexo
    def introducirSexo(self, sexo):
        if sexo != "F" or "M":
            self.__sexo="M"

    #Método ToString
    def __str__(self):
        return "Nombre: "+self.__nombre+" | Edad: "+str(self.__edad)+" | DNI: "+self.__dni+" | Sexo: "+self.__sexo+" | Peso: "+str(self.__peso)+" | Altura: "+str(self.__altura)
        #Para llamarlo: print(persona)

    #Método para generar DNI
    def generaDni(self):
        list_dni = [7]
        for i in range (7):
            list_dni.append(random.randint(0,9))

        palabra = "TRWAGMYFPDXBNJZSQVHLCKE"

        conv = [str(integer) for integer in list_dni]
        numero = "".join(conv)

        nif = int(numero)
        strnif = str(nif)

        letra = palabra[nif%23]

        dni = strnif + letra
        return dni
#3 objetos
if __name__ == "__main__":

    p = Persona(nombre=input("Introduzca nombre: "), edad=int(input("Introduzca edad: ")), dni=Persona.generaDni("") ,sexo=input("Introduzca sexo: "), peso=int(input("Introduzca peso: ")), altura=float(input("Introduzca altura: ")))

    if (p.calcularIMC(p.getpeso(), p.getaltura())) == -1:
        print("Su IMC indica que está por debajo de su peso ideal")
    elif (p.calcularIMC(p.getpeso(), p.getaltura())) == 0:
        print("Su IMC indica que está en su peso ideal")
    elif (p.calcularIMC(p.getpeso(), p.getaltura())) == 1:
        print("Su IMC indica que está por encima de su peso ideal")

    if (p.esMayordeEdad(p.getedad())) == True:
        print("Es mayor de edad")
    elif (p.esMayordeEdad(p.getedad()))==False:
        print("No es mayor de edad")

    print(p)


    p1 = Persona(nombre=p.getnombre(), edad=p.getedad(), dni=Persona.generaDni("") ,
                sexo=p.getsexo())

    if p1.getpeso()>0 and p1.getaltura()>0:
        if (p1.calcularIMC(p1.getpeso(), p1.getaltura())) == -1:
            print("Su IMC indica que está por debajo de su peso ideal")
        elif (p1.calcularIMC(p1.getpeso(), p1.getaltura())) == 0:
            print("Su IMC indica que está en su peso ideal")
        elif (p1.calcularIMC(p1.getpeso(), p1.getaltura())) == 1:
            print("Su IMC indica que está por encima de su peso ideal")

        if (p1.esMayordeEdad(p1.getedad())) == True:
            print("Es mayor de edad")
        elif (p1.esMayordeEdad(p1.getedad()))==False:
            print("No es mayor de edad")
    elif p1.getpeso() ==0 and p1.getaltura()==0:
        print("No se puede calcular el IMC")

    if (p1.esMayordeEdad(p1.getedad())) == True:
        print("Es mayor de edad")
    elif (p1.esMayordeEdad(p1.getedad()))==False:
        print("No es mayor de edad")

    print(p1)

    p2 = Persona()
    print(p2)
