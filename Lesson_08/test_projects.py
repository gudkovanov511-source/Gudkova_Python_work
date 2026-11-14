def test_create_project_positive(project_client, user_id):
    users = {user_id: "admin"}
    response = project_client.create("Новый проект", users)

    assert response.status_code == 201
    data = response.json()
    assert "id" in data

    project_client.delete_project(data["id"])


def test_create_project_negative(project_client, user_id):
    users = {user_id: "admin"}
    response = project_client.create("", users)

    assert response.status_code == 400


def test_create_project_negative_invalid_token(invalid_client, user_id):
    users = {user_id: "admin"}
    response = invalid_client.create("Проект", users)

    assert response.status_code == 401


def test_search_project_by_id(project_client, create_project):
    response = project_client.get_project(create_project)

    assert response.status_code == 200
    assert response.json()["id"] == create_project


def test_get_project_negative_not_found(project_client):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = project_client.get_project(fake_id)

    assert response.status_code == 404


def test_update_project_positive(project_client, create_project):
    response = project_client.update_project(
        create_project, "Переименованный проект")

    assert response.status_code == 200
    assert response.json()["id"] == create_project

    get_response = project_client.get_project(create_project)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Переименованный проект"


def test_update_project_negative(project_client):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = project_client.update_project(
        fake_id, "Переименованный проект")

    assert response.status_code == 404


def test_delete_project(project_client, create_project):
    response = project_client.delete_project(create_project)

    assert response.status_code == 200

    get_response = project_client.get_project(create_project)
    assert get_response.status_code == 200

    list_response = project_client.get_projects()
    assert list_response.status_code == 200

    titles = [p["title"] for p in list_response.json()["content"]]
    assert "Временный проект" not in titles
