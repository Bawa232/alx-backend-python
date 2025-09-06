#!/usr/bin/env

from mysql.connector import connect, Error

def connect_db():
    try:
        return connect(host='localhost', user='root', password='password')
    except Error as e:
        print(e)


def create_database(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE IF NOT EXISTS ALX_prodev')
    except Error as e:
        print(e)


def connect_to_prodev():
    try:
        return connect(host='localhost', user='root', password='password', database='ALX_prodev')
    except Error as e:
        print(e)


def create_table(connection):
    query = '''CREATE TABLE IF NOT EXISTS user_data (
    user_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age DECIMAL NOT NULL
    )'''

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
    except Error as e:
        print(e)



if __name__ == '__main__':
    conn_db = connect_db()
    create_database(conn_db)
    conn_prodev = connect_to_prodev()
    create_table(conn_prodev)
    insert_data(conn_prodev,
        {
            "uuid": "3crgsidhj-bc93-3ed0-b230-79832hjfb",
            "name": "James Bawa",
            "email": "jbawa032@gmail.com",
            "age": 27
        }
    )
    conn_db.close()
    conn_prodev.close()