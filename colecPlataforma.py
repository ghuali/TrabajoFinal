from db import Db
from plataforma import Plataforma

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS plataforma (
	id INTEGER  AUTOINCREMENT,
   	nombre TEXT NOT NULL PRIMARY KEY
)
'''

SQLDDLSELECT = '''
    SELECT * FROM plataforma
'''

SQLDDLINSERT = '''INSERT INTO plataforma (nombre) VALUES '''
                #Hay que concatenar  ('nombre')

SQLDDLUPDATEPART1 = '''UPDATE plataforma SET nombre = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM plataforma WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM plataforma WHERE nombre LIKE '''
                #Hay que concatenar



class ColeccionPlataforma:
    DBNAME = 'juegos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, plataforma):
        if self.buscar(plataforma) == 0:
            elstr = "('" + str(plataforma) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldplataforma:str, newplataforma:str):
        id = self.buscar(oldplataforma)
        if id != 0 and self.buscar(newplataforma) == 0:
            elstr = SQLDDLUPDATEPART1 + newplataforma 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, plataforma):
        id = self.buscar(plataforma) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, plataforma:Plataforma) -> int:
        resultado = 0
        elstr = '"' + str(plataforma) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado