from teacherTable import TeacherTable

db = TeacherTable(
    "postgresql://postgres:postgres12345@localhost:5432/QA"
    )


def test_create_teacher():
    teacher_id = db.get_next_teacher_id()
    email = "sombody@gmail.com"
    group_id = 125
    new_teacher = db.create_teacher(teacher_id, email, group_id)

    try:
        assert new_teacher["email"] == "sombody@gmail.com"
        assert new_teacher["group_id"] == 125
        assert new_teacher["teacher_id"] == teacher_id
    finally:
        db.delete_teacher_by_id(teacher_id)


def test_update_teacher():
    teacher_id = db.get_next_teacher_id()
    old_email = "sombody@gmail.com"
    old_group_id = 125
    db.create_teacher(teacher_id, old_email, old_group_id)

    try:
        new_email = "new@gmail.com"
        new_group_id = 120
        update_teacher = db.update_teacher(new_email, new_group_id, teacher_id)

        assert update_teacher["email"] == "new@gmail.com"
        assert update_teacher["group_id"] == 120
        assert update_teacher["teacher_id"] == teacher_id
    finally:
        db.delete_teacher_by_id(teacher_id)


def test_delete_teacher():
    teacher_id = db.get_next_teacher_id()
    email = "sombody@gmail.com"
    group_id = 125
    db.create_teacher(teacher_id, email, group_id)
    db.delete_teacher_by_id(teacher_id)

    assert db.get_teacher_by_id(teacher_id) is None
