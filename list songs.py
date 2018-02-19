import sqlite3
connection = sqlite3.connect("playlists") 
cursor = connection.cursor()
sql= """CREATE TABLE IF NOT EXISTS songs
        (SNAME VARCHAR(100),
         LENGTH INT,
         ARTIST VARCHAR(100),
         GENRE VARCHAR(100))"""
cursor.execute(sql)

sql = "SELECT * from songs"
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
           print ("name = ", row[0])
           print ("length = ", row[1])
           print ("artist = ", row[2])
           
           print ("genre = ", row[3],"\n")
