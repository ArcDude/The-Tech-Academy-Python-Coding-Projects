
import sqlite3

conn = sqlite3.connect('academy.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file1 TEXT, \
        col_file2 TEXT, \
        col_file3 TEXT, \
        col_file4 TEXT, \
        col_file5 TEXT, \
        col_file6 TEXT, \
        col_file7 TEXT, \
        col_file8 TEXT, \
        col_file9 TEXT, \
        col_file10 TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('academy.db')

with conn:
    cur = conn.cursor()
    cur.execute ("INSERT INTO tbl_fileList(col_file1, col_file2, col_file3, col_file4,\
                col_file5, col_file6, col_file7, col_file8, col_file9, col_file10) VALUES (?,?,?,?,?,?,?,?,?,?)", \
                ('information.docx', 'Am I.txt', 'myImage.png', 'myMovie.mpg', 'Closer?.txt',\
                 'data.pdf', 'myPhoto.jpg','annimation.gif', 'word.doc', 'myMusic.mp3'))
    conn.commit()
conn.close()


conn = sqlite3.connect('academy.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file2, col_file5 FROM tbl_fileList")
    conn.commit()
    varText = cur.fetchall()
    for text in varText:
        msg = "File Name1: {}\nFile Name2: {}".format(text[0], text[1])
    print(msg)
conn.close()
