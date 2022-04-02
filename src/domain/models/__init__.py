from peewee import Database, SqliteDatabase


def get_sqlite_connection():
    return SqliteDatabase(".db/vote.db")


def initialize_db(models, connection: Database):    
    connection.connect()
    connection.create_tables(models=models)


connection = get_sqlite_connection()
