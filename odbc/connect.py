import psycopg2
from decouple import config

"""
Foi necessário dar permissões ao usuário para acessar os dados.
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO empresa_user;
"""

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

        # Execute a query
        cur.execute("SELECT a.codigo, a.descricao FROM atividade a, projeto p, atividade_projeto ap WHERE ap.codProjeto = p.codigo AND p.codigo = 2 GROUP BY a.codigo")

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


if __name__ == '__main__':
    connect()