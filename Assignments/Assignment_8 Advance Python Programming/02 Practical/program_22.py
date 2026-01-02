# 22) Write a Python program to insert data into an SQLite3 database and fetch it.
import sqlite3

con = sqlite3.connect("mydb.db")
cur = con.cursor()

try:
    # Insert data
    cur.execute(
        "INSERT INTO Students VALUES (?, ?, ?)",
        (34, "Vinod", "3455342323")
    )
    con.commit()
    print("Insertion successful")

    # Fetch data
    cur.execute("SELECT * FROM Students")
    data = cur.fetchall()

    print("\nStudent Records:")
    for row in data:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    con.close()
