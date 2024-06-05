class Genero:
    def __init__(self,genero:str) -> None:
        self.genero = genero
    
    def __str__(self) -> str:
        return self.genero
    
    def leer(self) -> str:
        return self.genero