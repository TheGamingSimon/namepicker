import psycopg2

class Database:
    def __init__(self):
        self.params = {
            "dbname": "namepicker",
            "user": "postgres",
            "password": "postgres",
            "host": "localhost",
            "port": "5432"
        }
        self.connection = None

    def get_connection(self):
        try:
            if self.connection is None or self.connection.closed != 0:
                self.connection = psycopg2.connect(**self.params)
            return self.connection
        except Exception as e:
            print(f"Fehler beim Verbindungsaufbau: {e}")
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Datenbankverbindung geschlossen.")