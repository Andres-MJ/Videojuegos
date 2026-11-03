import sqlite3

def abrir_conexion():
    conexion = sqlite3.connect("videojuegos.db")
    return conexion

def crear_tabla():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        stock INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()