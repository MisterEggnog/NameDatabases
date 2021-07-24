#!/usr/bin/env python3

namesTable = '''CREATE TABLE names
                (name text, lang text)'''
addFirstName = '''INSERT INTO names (name)
                  VALUES (?)'''

import sqlite3

con = sqlite3.connect('names.db')

con.execute(namesTable)

con.commit()

con.close()
