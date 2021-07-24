#!/usr/bin/env python3

namesTable = '''CREATE TABLE names
                (name text, lang text)'''

import sqlite3

con = sqlite3.connect('names.db')

con.execute(namesTable)

con.commit()

con.close()
