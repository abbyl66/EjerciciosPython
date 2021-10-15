import Lavadora


class Electrodomesticos:

    #Constructor
    def __init__(self, pvbase= 100, color="Blanco", consEnerg="F", peso=5):
        self.__pvbase= pvbase
        self.__color = color
        self.__consEnerg = consEnerg
        self.__peso = peso

    #Métodos get

    def getpvbase (self):
        return self.__pvbase
    def getcolor (self):
        return self.__color
    def getconsEnerg (self):
        return self.__consEnerg
    def getpeso (self):
        return self.__peso

    #Método comprobar letra
    def comprobarComsumoE(self):

        if self.__consEnerg not in ("A", "B", "C", "D", "E", "F"):
            self.__consEnerg = "F"

    #Método String
    def __str__(self):
        return "Precio: " +str(self.__pvbase)+ " | Color: " +str(self.__color)+ " | Consumo Energía: " +str(self.__consEnerg)+ " | Peso: "+str(self.__peso)

    #Método comprobar color
    def comprobarcolor(self):

        if self.__color not in ("Blanco", "Azul", "Negro", "Rojo", "Gris") :
            self.__color = "Blanco"

    #Método precio final
    def precioFinalc(self):
        if self.__consEnerg == "A" and "a":
            self.__pvbase = int(self.__pvbase) + 100
        elif self.__consEnerg == "B" and "b":
            self.__pvbase = int(self.__pvbase) + 80
        elif self.__consEnerg == "C" and "c":
            self.__pvbase = int(self.__pvbase) + 60
        elif self.__consEnerg == "D" and "d":
            self.__pvbase = int(self.__pvbase) + 50
        elif self.__consEnerg == "E" and "e":
            self.__pvbase = int(self.__pvbase) + 30
        elif self.__consEnerg == "F" and "f":
            self.__pvbase = int(self.__pvbase) + 10

    def precioFinalp(self):
        if int(self.__peso) <= 0 and int(self.__peso) >= 19:
            self.__pvbase = int(self.__pvbase) + 10
        elif int(self.__peso) <= 20 and int(self.__peso) >=49:
            self.__pvbase = int(self.__pvbase) + 50
        elif int(self.__peso) <= 50 and int(self.__peso) >= 79:
            self.__pvbase = int(self.__pvbase) + 80
        elif int(self.__peso) >= 80:
            self.__pvbase = int(self.__pvbase) + 100

if __name__ == "__main__":

    lista_elect = ()
    lista_elect =list(lista_elect)

    lista_elect.insert(0, Electrodomesticos(pvbase=input("Introduzca el precio: "), color=input("Introduzca el color: "),
                           consEnerg=input("Introduzca el consumo: "), peso=input("Introduzca el peso: ")))
    lista_elect.insert(1, Electrodomesticos(pvbase=input("Introduzca el precio: "), color=input("Introduzca el color: "),
                           consEnerg=input("Introduzca el consumo: "), peso=input("Introduzca el peso: ")))


