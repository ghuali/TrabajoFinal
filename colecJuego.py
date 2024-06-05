from db import Db
from juego import Juego

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS juego (
	id INTEGER  AUTOINCREMENT,
   	nombre TEXT NOT NULL PRIMARY KEY
)
'''

SQLDDLSELECT = '''
    SELECT * FROM juego
'''

SQLDDLINSERT = '''INSERT INTO juegos (juego) VALUES '''
                #Hay que concatenar  ('juego')

SQLDDLUPDATEPART1 = '''UPDATE juego SET juego = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM juegos WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM juegos WHERE juego LIKE '''
                #Hay que concatenar



class ColeccionJuego:
    DBNAME = 'juegos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, juego):
        if self.buscar(juego) == 0:
            elstr = "('" + str(juego) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldjuego:str, newjuego:str):
        id = self.buscar(oldjuego)
        if id != 0 and self.buscar(newjuego) == 0:
            elstr = SQLDDLUPDATEPART1 + newjuego 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, juego):
        id = self.buscar(juego) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, juego:Juego) -> int:
        resultado = 0
        elstr = '"' + str(juego) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado