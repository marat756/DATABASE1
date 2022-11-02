import sqlite3 as sql

boglanish = sql.connect("sima.db")

malumot = boglanish.cursor()

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Bino(
    nomi TEXT,
    mavqiyi TEXT,
    baladligi INTEGER
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Davlat(
    nomi TEXT,
    strana TEXT,
    qalq soni INTEGER
)
""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Oqituvshi(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    ishi TEXT
)

""")