class Plataforma:
    def __init__(self,plataforma:str) -> None:
        self.plataforma = plataforma
    
    def __str__(self) -> str:
        return self.plataforma
    
    def leer(self) -> str:
        return self.plataforma