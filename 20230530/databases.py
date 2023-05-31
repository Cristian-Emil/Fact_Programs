import sqlite3

connection = sqlite3.connect('itf_database.db')
# connection.execute("DROP TABLE studenti")
# connection.execute("CREATE TABLE studenti ("
#                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                    "nume VARCHAR(50),"
#                    "prenume VARCHAR(50),"
#                    "varsta INTEGER,"
#                    "medie DOUBLE,"
#                    "data_inrolarii DATE"
#                    ")")
# connection.commit()

# connection.execute("ALTER TABLE studenti ADD COLUMN profesor VARCHAR(100)")
# connection.commit()

# connection.execute("DELETE FROM studenti")
# connection.commit()

# connection.execute("INSERT INTO studenti(nume, prenume, varsta, medie, data_inrolarii) VALUES "
#                    "(\"Nicolae\", \"Petru\", 23, 8.29, \"2021-09-10\"),"
#                    "(\"Costache\", \"Marcela\", 30, 9, \"2022-06-21\"),"
#                    "(\"Pop\", \"Andreea\", 36, 7.90, \"2021-02-03\")")
# connection.commit()

# connection.execute("UPDATE studenti SET profesor=\"Andreescu Mihai\" WHERE nume=\"Costache\"")
# connection.commit()

# connection.execute("INSERT INTO studenti(nume, prenume, varsta, data_inrolarii) VALUES "
#                    "(\"Badea\", \"Lucian\", 25, \"2023-04-11\")")
# connection.commit()

# connection.execute("UPDATE studenti SET medie=6 WHERE nume=\"Badea\" and prenume=\"Lucian\"")
# connection.commit()

# connection.execute("DELETE FROM studenti WHERE nume=\"Pop\" and prenume=\"Andreea\"")
# connection.commit()

# connection.execute("INSERT INTO studenti(nume, prenume, varsta, data_inrolarii) VALUES "
#                    "(\"Stefan\", \"Mirela\", 46, \"2023-04-11\")")
# connection.commit()

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM studenti WHERE medie > 7")
#
# studenti = cursor.fetchall()
# print(studenti)
#
# cursor.close()

# cursor = connection.cursor()
# cursor.execute("SELECT * FROM studenti")
#
# student1 = cursor.fetchone()
# print(student1)
#
# student2 = cursor.fetchone()
# print(student2)
#
# student = cursor.fetchone()
# while student:
#     print(student)
#     student = cursor.fetchone()
#
#
# cursor.close()

cursor = connection.cursor()
cursor.execute("SELECT * FROM studenti s "
               "JOIN profesori p "
               "ON s.profesor = (p.nume || \" \" || p.prenume)"
               "WHERE s.profesor NOT NULL")

print(cursor.fetchall())

connection.close()
