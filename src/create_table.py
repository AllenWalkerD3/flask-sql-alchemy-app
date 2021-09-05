import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

create_table = "create table if not exists tbl_user (id integer primary key, username text, password text)"
cursor.execute(create_table)

create_table = "create table if not exists tbl_item (id integer primary key, name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()