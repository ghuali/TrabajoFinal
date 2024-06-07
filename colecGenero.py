from db import Db
from genero import Genero

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS genero (
	id INTEGER  AUTOINCREMENT,
   	nombre TEXT NOT NULL PRIMARY KEY
)
'''

SQLDDLSELECT = '''
    SELECT * FROM genero
'''

SQLDDLINSERT = '''INSERT INTO genero (nombre) VALUES '''
                #Hay que concatenar  ('nombre')

SQLDDLUPDATEPART1 = '''UPDATE genero SET nombre = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM genero WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM genero WHERE nombre LIKE '''
                #Hay que concatenar



class ColeccionGenero:
    DBNAME = 'juegos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, genero):
        if self.buscar(genero) == 0:
            elstr = "('" + str(genero) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldgenero:str, newgenero:str):
        id = self.buscar(oldgenero)
        if id != 0 and self.buscar(newgenero) == 0:
            elstr = SQLDDLUPDATEPART1 + newgenero 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, genero):
        id = self.buscar(genero) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, genero:Genero) -> int:
        resultado = 0
        elstr = '"' + str(genero) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado