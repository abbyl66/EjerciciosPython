from Electrodomesticos import Electrodomesticos

class Television(Electrodomesticos):
    __res = 20
    __fourK = False

    def __int__(self, pvbase, color, consEnerg, peso, res, fourK):
        Electrodomesticos.__init__(self, pvbase, color, consEnerg, peso)
        __res = res
        __fourK = fourK

    def getres(self):
        return self.__res
    def getfourK (self):
        return self.getres()

    def precioFin(self):
        if self.__res > 40:
            super().__pvbase = int(super().__pvbase) * 1.3

        if self.__fourK == True:
            super().__pvbase = int(super().__pvbase) +50
