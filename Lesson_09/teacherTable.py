from sqlalchemy import create_engine, text


class TeacherTable:
    __scripts = {
        "insert_new": text(
            "INSERT INTO teacher (\"email\", \"group_id\") "
            "VALUES (:new_email, :new_group_id) "
            "RETURNING teacher_id, email, group_id"
        ),
        "search_by_email": text(
            "SELECT * FROM teacher WHERE email = :email"
        ),
        "search_by_id": text(
            "SELECT * FROM teacher WHERE teacher_id = :t_id"
        ),
        "deleted_by_id": text(
            "DELETE FROM teacher WHERE teacher_id = :t_id"
        ),
        "update_teacher": text(
            "UPDATE teacher SET email = :new_email, group_id = :new_group_id "
            "WHERE teacher_id = :t_id "
            "RETURNING teacher_id, email, group_id"
        )
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_teacher(self, email, group_id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["insert_new"],
            {"new_email": email, "new_group_id": group_id}
            )
        conn.commit()
        new_teacher = result.mappings().first()
        conn.close()
        return new_teacher

    def get_teacher_by_email(self, email):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["search_by_email"],
                              {"email": email})
        found_teacher = result.mappings().first()
        conn.close()
        return found_teacher

    def get_teacher_by_id(self, teacher_id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["search_by_id"],
                              {"t_id": teacher_id})
        found_teacher = result.mappings().first()
        conn.close()
        return found_teacher

    def delete_teacher_by_id(self, teacher_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["deleted_by_id"],
                     {"t_id": teacher_id})
        conn.commit()
        conn.close()

    def update_teacher(self, email, group_id, teacher_id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["update_teacher"],
                              {
                                "new_email": email,
                                "new_group_id": group_id,
                                "t_id": teacher_id
                                }
                              )
        conn.commit()
        up_teacher = result.mappings().first()
        conn.close()
        return up_teacher
