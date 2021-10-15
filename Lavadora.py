from Electrodomesticos import Electrodomesticos

class Lavadora (Electrodomesticos):

    def __int__(self, pvbase=100, color="Blanco", consEnerg="F", peso=5, carga=5):
        Electrodomesticos.__init__(self, pvbase=pvbase, color=color, consEnerg=consEnerg, peso=peso)
        self.carga=carga

    def getcarga (self):
        return self.__carga

    def precioFinal(self):
        if self.carga > 30:
            super().__pvbase = super().__pvbase+50


