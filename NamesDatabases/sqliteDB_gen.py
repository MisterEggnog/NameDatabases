#!/usr/bin/env python3
import sqlite3
import os

database = 'names.db'
namesTables = '''CREATE TABLE first_names
                (name text)'''
addFirstName = '''INSERT INTO first_names (name)
                  VALUES (?)'''

# Try to remove old database
try:
    os.remove(database)
except:
    pass

con = sqlite3.connect(database)

# Create tables
con.execute(namesTables)

con.commit()

con.close()
