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
        if self.__consEnerg == "A" or "a":
            self.__pvbase = int(self.__pvbase) + 100
        elif self.__consEnerg == "B" or "b":
            self.__pvbase = int(self.__pvbase) + 80
        elif self.__consEnerg == "C" or "c":
            self.__pvbase = int(self.__pvbase) + 60
        elif self.__consEnerg == "D" or "d":
            self.__pvbase = int(self.__pvbase) + 50
        elif self.__consEnerg == "E" or "e":
            self.__pvbase = int(self.__pvbase) + 30
        elif self.__consEnerg == "F" or "f":
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


#CLASE LAVADORA
class Lavadora(Electrodomesticos):

    def __init__(self, pvbase, color, consEnerg, peso, carga=5):
       Electrodomesticos.__init__(self, pvbase, color, consEnerg, peso)
       self.__carga = carga

    def getcarga (self):
        return self.__carga

    def precioFinal(self):
        if self.__carga > 30:
            super().__pvbase = super().__pvbase+50

    def __str__(self):
        return super().__str__()+" | Carga : " +str(self.__carga)


#CLASE TELEVISION
class Television(Electrodomesticos):

    def __init__(self, pvbase, color, consEnerg, peso, res=20, fourK=False):
        Electrodomesticos.__init__(self, pvbase, color, consEnerg, peso)
        self.__res = res
        self.__fourK = fourK

    def getres(self):
        return self.__res
    def getfourK (self):
        return self.getres()

    def precioFin(self):
        if self.__res > 40:
            super().__pvbase = int(super().__pvbase) * 1.3

        if self.__fourK == True:
            super().__pvbase = int(super().__pvbase) +50

    def __str__(self):
        return super().__str__()+ " | Resolución: " +str(self.__res)+" | FourK: " +str(self.__fourK)

if __name__ == "__main__":

    lista_elect = ()
    lista_elect =list(lista_elect)

    lista_elect.insert(0, Electrodomesticos(pvbase=60, color="Rosa", consEnerg="A", peso=12))
    lista_elect.insert(1, Lavadora(pvbase=90, color="Gris", consEnerg="F", peso=15, carga=10))
    lista_elect.insert(2, Television(pvbase=50, color="Azul", consEnerg="B", peso=16, res=30, fourK=True))

    for x in range (0, len(lista_elect)):
        Electrodomesticos.comprobarcolor(lista_elect[x])
        Electrodomesticos.comprobarComsumoE(lista_elect[x])
        Electrodomesticos.precioFinalc(lista_elect[x])
        Electrodomesticos.precioFinalp(lista_elect[x])
    Lavadora.precioFinal(lista_elect[1])


    #Recorrer lista
    for x in range(0,len(lista_elect)):
        print(lista_elect[x])


