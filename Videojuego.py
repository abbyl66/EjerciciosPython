class Videojuego:

    #Constructor
    def __init__(self, titulo="", horasEst=10, genero="", compania=""):
        self.titulo = titulo
        self.horasEst = horasEst
        self.genero = genero
        self.compania = compania

    #Métodos get y set
    def settitulo (self, titulo):
        self.titulo = titulo
    def gettitulo (self):
        return self.titulo

    def sethorasEst (self, horasEst):
        self.horasEst = horasEst
    def gethorasEst (self):
        return self.horasEst

    def setgenero (self,genero):
        self.genero = genero
    def getgenero (self):
        return self.genero

    def setcompania (self, compania):
        self.compania = compania
    def getcompania (self):
        return self.compania

    #Método ToString
    def __str__(self):
        return "Titulo: "+self.titulo+" | Horas estimadas: "+str(self.horasEst)+" | Genero: "+self.genero+" | Compañía: "+self.compania

    def entregado(self):
        self.entregado=True

if __name__ == "__main__":
    list_videojuegos = [Videojuego(titulo="Call of duty", horasEst=5, genero="Animacion",compania="Justin Roiland, Dan Harmon"),
                        Videojuego(titulo="Mario Bros", horasEst=4, genero="Drama", compania="Elisa"),
                        Videojuego(titulo="League of Legends", horasEst=2, genero="Comedia", compania="Daniel"),
                        Videojuego(titulo="The binding of Isaac", horasEst=3, genero="Comedia", compania="Christian"),
                        Videojuego(titulo="Solitario", horasEst=2, genero="Tragedia", compania="Leo")]


