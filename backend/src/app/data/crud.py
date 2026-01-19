class SchuelerRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_name(self, name):
        conn = self.db_manager.get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO Schueler (name) VALUES (%s)", (name,))
                    conn.commit()
                    print(f"'{name}' wurde erfolgreich hinzugefügt.")
            except Exception as e:
                conn.rollback()

    def get_all_names(self):
        conn = self.db_manager.get_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Schueler")
                return cursor.fetchall()
        return []