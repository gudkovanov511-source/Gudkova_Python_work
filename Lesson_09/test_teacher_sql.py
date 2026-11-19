from teacherTable import TeacherTable

db = TeacherTable(
    "postgresql://postgres:postgres12345@localhost:5432/QA"
    )


def test_create_teacher():
    email = "sombody@gmail.com"
    group_id = 125
    new_teacher = db.create_teacher(email, group_id)

    try:
        assert new_teacher["email"] == "sombody@gmail.com"
        assert new_teacher["group_id"] == 125
        assert isinstance(new_teacher["teacher_id"], int)
    finally:
        t_id = new_teacher["teacher_id"]
        db.delete_teacher_by_id(t_id)


def test_update_teacher():
    old_email = "sombody@gmail.com"
    old_group_id = 125
    new_teacher = db.create_teacher(old_email, old_group_id)
    t_id = new_teacher["teacher_id"]

    new_email = "new@gmail.com"
    new_group_id = 120
    teacher_id = t_id

    try:
        update_teacher = db.update_teacher(new_email, new_group_id, teacher_id)
        assert update_teacher["email"] == "new@gmail.com"
        assert update_teacher["group_id"] == 120
        assert update_teacher["teacher_id"] == t_id
    finally:
        db.delete_teacher_by_id(teacher_id)


def test_delete_teacher():
    email = "sombody@gmail.com"
    group_id = 125
    new_teacher = db.create_teacher(email, group_id)
    t_id = new_teacher["teacher_id"]
    db.delete_teacher_by_id(t_id)

    assert db.get_teacher_by_id(t_id) is None
