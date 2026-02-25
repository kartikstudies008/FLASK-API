#---------CREATED DATA BASE ---------#

# import sqlite3

# conn = sqlite3.connect("student.db")

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                city TEXT            
# )
# """)

# print("TABLE IS CREATED")

# conn.commit()
# conn.close()

#--------INSERT INTO DATABASE ------#
# import sqlite3

# conn = sqlite3.connect("student.db")

# cursor = conn.cursor()

# cursor.execute("""
# INSERT INTO students (name,city)
# VALUES (?,?)
# """,("Kartik","Chandigarh"))

# conn.commit()

# print("STUDENT INSERTED DATA SUCCESFULLY")

# conn.close()

#-------READ DATA FROM DATABASE -------#
import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

    conn.close()