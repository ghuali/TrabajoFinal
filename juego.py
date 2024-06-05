class Juego:
    def __init__(self,juego:str) -> None:
        self.juego = juego
    
    def __str__(self) -> str:
        return self.juego
    
    def leer(self) -> str:
        return self.juego