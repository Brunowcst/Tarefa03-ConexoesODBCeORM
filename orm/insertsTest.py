import psycopg2
from decouple import config
from faker import Faker
import random

fake = Faker()


# config = config(".env")
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
        createDatas(conn, qntInserts)

        # Retrieve query results
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

def createDatas(conn, qntInserts):
    try:
        cur = conn.cursor()
        for i in range(qntInserts):
            insertFunc(cur)

        conn.commit()
        print('Dados inseridos com sucesso no banco de dados.')

    except (Exception, psycopg2.DatabaseError) as error:
        print('Erro ao inserir dados:', error)
    
def insertFunc(cur):
    sexos = ['M', 'F']
    nome = fake.name()
    datanasc = fake.date_of_birth(minimum_age=18, maximum_age=60)
    salario = fake.random_int(min=600, max=9500)
    depto = fake.random_int(min=1, max=2)
    sexo = random.choice(sexos)
    
    cur.execute("INSERT INTO funcionario (nome, datanasc, salario, depto, sexo) VALUES (%s, %s, %s, %s, %s)", (nome, datanasc, salario, depto, sexo))

if __name__ == '__main__':
    connect()