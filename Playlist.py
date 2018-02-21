import sqlite3
connection = sqlite3.connect("playlists") 
cursor = connection.cursor() 
#Create the table if one doesn’t yet exist
sql= """CREATE TABLE IF NOT EXISTS lists 
        (NAME VARCHAR(100),
         LENGTH INT)"""
cursor.execute(sql)

login = False
while login == False:
    q = input("""Hello would you like to:
    1) Login
    2) Create a new account
    : """)
    if q == "1":
        username = input("Username : ")
        password = input("Password : ")
        sql= """CREATE TABLE IF NOT EXISTS users 
        (USERNAME VARCHAR(100),
         PASSWORD VARCHAR(100))"""
        cursor.execute(sql)
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            if username in row[0] and password in row[1]:
                login = True
            else:
                print ("Login failed please try again...")
    elif q == "2":
        username = input("What would you like as your Username? : ")
        password = input("What would you like as your Password? : ")
        password2 = input("Please confirm your Password? : ")
        if password != password2:
            print ("Passwords error please Try again")
        elif password == password2:
            print("Password match!")
            
            print ("You have added the User : ", username, ":" ,password)
            sql = "INSERT into users (username, password) VALUES (?, ?)"
            cursor.execute(sql, (username ,password))
            connection.commit()
            login = True


while login is True:

    text = """Welcome to Songify username
    Please enter what you would like to do:
        1 ) Show all playlists
        2 ) Add a playlist
        3 ) Delete a playlist
        4 ) Add a song to a playlist
        5 ) Delete a song from a playlist
        6 ) Show all songs
        7 ) Logout
          : """
    customtext= text.replace("username",username)
    question = input(customtext)
    print ("\n")
    if question=="1":
        sql = "SELECT * from lists"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
           print (" = ", row[0])
           sqlprint = "SELECT * from ?"
           sqlnew= sqlprint.replace("?",row[0])
           cursor.execute(sqlnew)
           rows = cursor.fetchall()
           for row in rows:
                print("    - ", row[0]," ",row[1])
        print ("\n")      
           
           
    if question=="2":
        playlistname = input("What would you like to call your playlist? :")
        create = input("Are you sure you would like to create this playlist? Y/N :")
        confirm = False
        if create in ("Y","y"):
            confirm = True
        if confirm == True:
            sql= """CREATE TABLE IF NOT EXISTS ?
                    (SNAME VARCHAR(100),
                     SLENGTH INT)"""
            sqlnew= sql.replace("?",playlistname.lower())
            cursor.execute(sqlnew)
            
            sql = "INSERT into Lists(NAME)VALUES (?)"
            cursor.execute(sql,(playlistname.lower(),))
            connection.commit()
            print ("Playlist base created called "+ playlistname)
        print ("\n")
        
    elif question=="3":
        playlistname = input("What playlist would you like to delete? :")
        delete = input("Are you sure you would like to delete this playlist? Y/N :")
        if delete in ("Y","y"):
            sql = "DELETE FROM lists WHERE Name=?"
            cursor.execute(sql,(playlistname.lower(),))
            connection.commit()
            sql = "DROP TABLE list"
            sqlreplace = sql.replace("list",playlistname)
        print ("\n")    

    elif question=="4":
        sql = "SELECT * from Lists"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print ("Playlists : ")
        for row in rows:
           print (" - " , row[0])
        print ("\n")

        playlistadd = input("What Playlist would you like to add your song to? :")
        songname = input("What song would you like to add? : ")
        songname = songname.lower()
        playlistadd = playlistadd.lower()

        sql = "SELECT * FROM lists"
        cursor.execute(sql)
        rows = cursor.fetchall()
        found = False
        foundplay= False
        for row in rows:
            if playlistadd == row[0] :
                
                sql = "SELECT * FROM songs"
                cursor.execute(sql)
                rows = cursor.fetchall()
                foundplay = True
                for row in rows:
                    if songname == row[0] :
                        sql = "INSERT into playlist (SNAME, SLENGTH) VALUES (?, ?)"
                        sqlreplace = sql.replace("playlist",playlistadd)
                        cursor.execute(sqlreplace,(row[0],row[1]))
                        connection.commit()
                        found = True
                if found == False:
                    print ("Song not found ... ")
                elif found == True:
                    print ("Song added to the playlist")

            if foundplay == False:
                print ("Playlist Not found!")
        print ("\n")
        
    elif question=="5":
        sql = "SELECT * from Lists"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print ("Playlists : ")
        for row in rows:
           print (" - " , row[0])
        print ("\n")

        playlistadd = input("What Playlist would you like to delete your song from? :")
        songname = input("What song would you like to delete? : ")
        songname = songname.lower()
        playlistdel = playlistadd.lower()

        sql = "SELECT * FROM lists"
        cursor.execute(sql)
        rows = cursor.fetchall()
        found = False
        for row in rows:
            if playlistadd == row[0] :
                sql = "SELECT * FROM songs"
                cursor.execute(sql)
                rows = cursor.fetchall()
                delete = False
                for row in rows:
                    if songname == row[0] :
                        sql = "DELETE FROM playlist WHERE SNAME=?"
                        sqlreplace = sql.replace("playlist",playlistdel)
                        cursor.execute(sqlreplace,(row[0],))
                        connection.commit()
                        delete = True
                if delete == False:
                    print ("Song or playlist not found ... ")
                elif delete == True:
                    print ("Song deleted from the playlist")

            elif playlistadd != row[0]:
                print ("Playlist Not found!")
        print ("\n")

    elif question=="6":
        sql = "SELECT * from songs"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
           print ("name = ", row[0])
           print ("length = ", row[1])
           print ("artist = ", row[2])
           
           print ("genre = ", row[3],"\n")

    elif question=="7":
        login = False
	

