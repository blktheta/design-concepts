import sqlite3


con = sqlite3.connect('application.db')

cur = con.cursor()

# create table
cur.execute('''
    CREATE TABLE blogs (
        id TEXT NOT NULL PRIMARY KEY,
        date TEXT,
        title TEXT,
        content TEXT,
        public INTEGER
    )
''')

# insert a few rows of data
cur.execute("INSERT INTO blogs VALUES ('first-blog', '2021-03-07', 'My first blog', 'Some content', 1)")
cur.execute("INSERT INTO blogs VALUES ('private-blog', '2021-03-07', 'Secret blog', 'This is a secret', 0)")

# save (commit) the changes
con.commit()

# close the connection
con.close()
