import sqlite3
connection = sqlite3.connect("playlists") 
cursor = connection.cursor()
sql= """CREATE TABLE IF NOT EXISTS songs
        (SNAME VARCHAR(100),
         LENGTH INT,
         ARTIST VARCHAR(100),
         GENRE VARCHAR(100))"""
cursor.execute(sql)

songname =input(" What is the name of the SONG you would like to add? : ")
artist =input(" Who wrote it? ")
length =input(" How long is it in seconds? : ")
genre =input(" What genre is it? : ")


songname = songname.lower()
artist = artist.lower()

length = length.lower()
genre = genre.lower()

sql = "INSERT into songs (SNAME, ARTIST ,LENGTH, GENRE) VALUES (?, ?, ?, ?)"
cursor.execute(sql, (songname, artist ,length ,genre))
connection.commit()
