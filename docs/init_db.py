import sqlite3

connection = sqlite3.connect('database.db')


with open('docs\schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO announcements (title, announcementText) VALUES (?, ?)",
            ("First Announcement!","Here you can put announcements!")
            )

connection.commit()
connection.close()
