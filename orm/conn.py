import psycopg2
from decouple import config
from generator import createDatas
from models import *

# Configurações do banco de dados
NAME = config('DATABASE_NAME')
USER = config('DATABASE_USER')
PASSWORD = config('DATABASE_PASS')
HOST = config('DATABASE_HOST')
PORT = config('DATABASE_PORT')
DEBUG = config('DEBUG', cast=bool, default=False)


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=HOST,
            database=NAME,
            user=USER,
            password=PASSWORD,
            port=PORT
        )

        # Set database connection for models
        # Funcionario._meta.database = conn
        # Departamento._meta.database = conn


        # create tables if they don't exist
        # conn.create_tables([Funcionario, Departamento])

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # Cria os dados
        qntInserts = int(input("Digite a quantidade de dados a serem gerados:"))
        createDatas(qntInserts, cur)

        # Retrieve query results
        cur.execute('SELECT * FROM funcionario')
        records = cur.fetchall()
        print("Total number of rows:", cur.rowcount)
        for row in records:
            print(row)

        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def main():
    connect()

if __name__ == '__main__':
    main()