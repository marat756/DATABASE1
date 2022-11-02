import sqlite3 as sql

boglanish = sql.connect("hiro.db")

malumot = boglanish.cursor()

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Kompyter(
    nomi TEXT,
    rxotirasi TEXT,
    narxi INTEGER
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Telepon(
    nomi TEXT,
    ishlav shiqaruvshi TEXT,
    bohosi INTEGER,
    soni INTEGER
)
""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Dangasa(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    ishi TEXT
)

""")