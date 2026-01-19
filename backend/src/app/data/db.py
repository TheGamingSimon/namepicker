import os
import psycopg2
from psycopg2.extensions import connection as PgConnection

class Database:
    def __init__(self):
        self.dsn = os.getenv("DATABASE_URL")
        self.connection = None

    def connect(self) -> PgConnection:
        return psycopg2.connect(self.dsn)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Datenbankverbindung geschlossen.")