import sqlite3

# making a connection, the cursor is like our handle
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# drop the table if it exists, so we start fresh
cur.execute('DROP TABLE IF EXISTS Counts')

# we pretend its a dictionary = an in-memory database
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# get a filename (fname)
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
# loop through it
for line in fh:
    if not line.startswith('From: '): continue # makes sure we can only get the from lines
    pieces = line.split()
    email = pieces[1] # grab the email adress
    # dictionary part
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))  # the ? = placeholder which can be replaced by the email later
    row = cur.fetchone() # grab the 1st one, and give it back in a row
    if row is None: # if there are no records, there wont be any rows
            cur.execute('''INSERT INTO Counts (email, count)
                        VALUES (?, 1)''', (email,)) # its the first time we see it, thats why we need to set it to 1 with the email having the ? placeholder
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', # if there is one that exists, this turns whatever number there is to one higher.
                    (email,))
    conn.commit() # at some point the database needs to write all the data to disc. this can take some time, so it's used a lot
    # adding new records !

#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' # selecting the top 10 emails

for row in cur.execute(sqlstr): # ask for the rows one at a time
    print(str(row[0]), row[1])

cur.close() # then we close the connection
