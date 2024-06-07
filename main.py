from colecJuego import ColeccionJuego
from juego import Juego

cc = ColeccionJuego()
#print(cc.leer())
#cc.buscar(Cita('La vida es bella'))

print(cc.buscar(Juego('La vida es bella')))
print(cc.insertar(Juego('Quedan 2 semanas de clase')))
cc.borrar(Juego('Aguanta ahí'))
cc.actualizar("Quedan 2 semanas de clase", "Hola qué tal!")
print(cc.leer())