from db import Db
from juego import Juego

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS juego (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	nombre TEXT NOT NULL 
)
'''

SQLDDLSELECT = '''
    SELECT * FROM juego
'''

SQLDDLINSERT = '''INSERT INTO juego (nombre) VALUES '''
                #Hay que concatenar  ('juego')

SQLDDLUPDATEPART1 = '''UPDATE juego SET nombre = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM juego WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM juego WHERE nombre LIKE '''
                #Hay que concatenar



class ColeccionJuego:
    DBNAME = 'juegos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, nombre):
        if self.buscar(nombre) == 0:
            elstr = "('" + str(nombre) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldnombre:str, newnombre:str):
        id = self.buscar(oldnombre)
        if id != 0 and self.buscar(newnombre) == 0:
            elstr = SQLDDLUPDATEPART1 + newnombre 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, nombre):
        id = self.buscar(nombre) 
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