#!/usr/bin/env python3
import sqlite3
import os

database = 'names.db'
namesTable = '''CREATE TABLE names
                (name text, lang text)'''
addFirstName = '''INSERT INTO names (name)
                  VALUES (?)'''

try:
    os.remove(database)
except:
    pass

con = sqlite3.connect(database)

con.execute(namesTable)

con.commit()

con.close()
