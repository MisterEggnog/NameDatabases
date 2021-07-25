#!/usr/bin/env python3
import os
from Pathlib import PurePath
import glob
import sqlite3

database = 'names.db'
firstNamesTable = '''CREATE TABLE first_names
                 (name text);'''
lastNamesTable = '''CREATE TABLE last_names
                    (name text, lang text)'''
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
cur.execute(firstNamesTable)
cur.execute(lastNamesTable)

# Load first names from 'first names'/all.txt
firstNames = open("first names/all.txt", "r", encoding='utf-8-sig')
lines = firstNames.readlines()
cur.executemany(addFirstName, map(lambda l : (l.strip(),), lines))
firstNames.close()

# Load last names from 'surnames/??.txt'
files = glob.glob('surnames/??.txt')
for file in files:
    lang = PurePath(file).stem

con.commit()

con.close()
