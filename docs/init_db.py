import sqlite3

connection = sqlite3.connect('database.db')


with open('docs\schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO announcements (title, announcementText) VALUES (?, ?)",
            ("First Announcement!","Here you can put announcements!")
            )


cur.execute("INSERT INTO tasks (title, descriptionText, subTaskOne, subTaskTwo) VALUES (?, ?, ?, ?)",
            ("First Task!","Here you can put the description!","Sub Task One!", "Sub Task Two!")
            )


connection.commit()
connection.close()
