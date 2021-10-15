
class Serie:

    #Constructor
    def __init__(self, titulo="", numTemp=3, genero="", creador=""):
        self.titulo = titulo
        self.numTemp = numTemp
        self.genero = genero
        self.creador = creador

    #Métodos get y set

    def settitulo (self, titulo):
        self.titulo = titulo
    def gettitulo (self):
        return self.titulo

    def setnumTemp (self, numTemp):
        self.numTemp = numTemp
    def getnumTemp (self):
        return self.numTemp

    def setgenero (self, genero):
        self.genero = genero
    def getgenero (self):
        return self.genero

    def setcreador (self, creador):
        self.creador=creador
    def getcreador (self):
        return self.creador

    #Método ToString
    def __str__(self):
        return "Titulo: "+self.titulo+" | Numero de temporadas: "+str(self.numTemp)+" | Género: "+self.genero+" | Creador: "+self.creador

    def entregado(self):
        self.entregado=True

if __name__ == "__main__":
    list_series = [Serie(titulo="Rick y Morty",numTemp=5,genero="Animacion",creador="Justin Roiland, Dan Harmon"),
                   Serie(titulo="Sabrina", numTemp=4, genero="Drama", creador="Elisa"),
                   Serie(titulo="Rebelde", numTemp=2, genero="Comedia", creador="Daniel"),
                   Serie(titulo="Vacaciones", numTemp=3, genero="Comedia", creador="Christian"),
                   Serie(titulo="Vlog", numTemp=2, genero="Tragedia", creador="Leo")]

    for i in list_series:
        print(i)




