# 21) Write a Python program to create a database and a table using SQLite3.
# import sqlite
import sqlite3

con = sqlite3.connect("mydb.db") #connect sqlite

qry = "create table Students (id integer,name text,mobile text)"

try:
    data  = con.execute(qry)
    print("database and table created")
except:
    print("error")

