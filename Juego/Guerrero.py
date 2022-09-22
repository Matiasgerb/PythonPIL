from Juego.Personaje import Personaje


class Guerrero(Personaje):
    def __init__(self,nombre,nivel,ataque,vida,defensa):
        self.nombre = nombre
        self.nivel = nivel
        self.ataque = ataque
        self.vida = vida
        self.defensa = defensa
        super().__init__()


g1=Guerrero('Matias',33,200,100,50)