class SchuelerRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_all_names(self, class_id: int):
        conn = self.db_manager.connect()
        if not conn:
            return []

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, vorname, nachname FROM names WHERE class_id = %s",
                    (class_id,)
                )
                return cursor.fetchall()
        except Exception as e:
            conn.rollback()
            raise e

        
    def create_student(self, vorname: str, nachname: str, class_id: int | None):
        conn = self.db_manager.connect()
        if not conn:
            return None

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO names (vorname, nachname, class_id)
                    VALUES (%s, %s, %s)
                    RETURNING id, vorname, nachname, class_id;
                    """,
                    (vorname, nachname, class_id),
                )
                result = cursor.fetchone()
                conn.commit()
                return result
        except Exception as e:
            conn.rollback()
            raise e
        
    def update_student(self, student_id: int, vorname: str, nachname: str, class_id: int | None):
        conn = self.db_manager.connect()
        if not conn:
            return None

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE names
                    SET vorname=%s, nachname=%s, class_id=%s
                    WHERE id=%s
                    RETURNING id, vorname, nachname, class_id;
                    """,
                    (vorname, nachname, class_id, student_id),
                )
                result = cursor.fetchone()
                conn.commit()
                return result
        except Exception as e:
            conn.rollback()
            raise e
        
    def delete_student(self, student_id: int):
        conn = self.db_manager.connect()
        if not conn:
            return False

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM names WHERE id=%s;",
                    (student_id,),
                )
                deleted = cursor.rowcount > 0
                conn.commit()
                return deleted
        except Exception as e:
            conn.rollback()
            raise e
        
    def pick_and_assign_students(self, class_id: int, count: int):
        conn = self.db_manager.connect()
        if not conn:
            return []

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id
                    FROM names
                    WHERE class_id IS NULL
                    ORDER BY random()
                    LIMIT %s;
                    """,
                    (count,)
                )
                rows = cursor.fetchall()
                student_ids = [r[0] for r in rows]

                if not student_ids:
                    return []

                cursor.execute(
                    """
                    UPDATE names
                    SET class_id = %s
                    WHERE id = ANY(%s)
                    RETURNING id, vorname, nachname, class_id;
                    """,
                    (class_id, student_ids),
                )

                result = cursor.fetchall()
                conn.commit()
                return result

        except Exception as e:
            conn.rollback()
            raise e

class ClassRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_classes(self):
        conn = self.db_manager.connect()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT name FROM classes")
                    return cursor.fetchall()
            except Exception as e:
                conn.rollback()

    def create_class(self, name: str):
        conn = self.db_manager.connect()
        if not conn:
            return None

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO classes (name) VALUES (%s) RETURNING id, name;",
                    (name,)
                )
                result = cursor.fetchone()
                conn.commit()
                return result
        except Exception as e:
            conn.rollback()
            raise e
