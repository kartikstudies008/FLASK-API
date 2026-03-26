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
# Import the sqlite3 module to work with SQLite databases
import sqlite3

# Open a connection to the student.db database file
conn = sqlite3.connect("student.db")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve all rows from the students table
cursor.execute("SELECT * FROM students")

# Fetch all results from the last executed query
rows = cursor.fetchall()

# Iterate over each row and print it to the console
for row in rows:
    print(row)

    # Close the database connection after reading (inside loop – closes after first row)
    conn.close()