def create_materia(self, conn, materia):
        try:
            sql = '''INSERT INTO
            users (nombre, alumno, calificacion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cur = conn.cursor()
            cur.execute(sql, materia)
            conn.commit()
            msg = "Registered Successfully"
        except:
            conn.rollback()
            msg = "Error occured"
        return msg