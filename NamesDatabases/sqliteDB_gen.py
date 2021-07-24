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
cur = con.cursor()

# Create tables
cur.execute(namesTables)

# Load first names from 'first names'/all.txt
firstNames = open("first names/all.txt", "r", encoding='utf-8-sig')
lines = firstNames.readlines()
cur.executemany(addFirstName, map(lambda l : (l.strip(),), lines))
firstNames.close()

con.commit()

con.close()
