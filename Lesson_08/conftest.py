import pytest
from yougile_project import YougileProject


API_KEY = "Ключ в файле"
BASE_URL = "https://ru.yougile.com/api-v2/"
USER_ID = "id в файле"

project = YougileProject(BASE_URL, API_KEY)


@pytest.fixture(scope="module")
def project_client():
    return project


@pytest.fixture(scope="module")
def user_id():
    return USER_ID


@pytest.fixture(scope="module")
def invalid_client():
    return YougileProject(BASE_URL, "invalid_token_12345")


@pytest.fixture(scope="module")
def create_project(project_client):
    users = {USER_ID: "admin"}
    response = project_client.create("Временный проект", users)
    project_id = response.json()["id"]

    yield project_id
    project_client.delete_project(project_id)
