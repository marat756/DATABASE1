import sqlite3 as sql

boglanish = sql.connect("fist.db")

malumot = boglanish.cursor()

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Falsafa(
    vazifasi TEXT,
    mondarijasi TEXT,
    bosib shiqarailgan sana INTEGER
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Pythonshi(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    kurs INTEGER
)
""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Flanetalar(
    nomi TEXT,
    shakli TEXT,
    yosh INTEGER,
    ikkinshi nomi TEXT
)

""")