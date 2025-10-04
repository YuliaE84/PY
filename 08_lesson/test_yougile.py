import requests
import pytest

base_url = "https://ru.yougile.com/api-v2"
key = "K8MBrJ6B+EVUaAfnuSgtdkh9iym+8J1RTiE0H3NhO7AacAaS71EEMQzkBJUP3GNP"

#позитивный тест
def test_create_project():
    new_project_name = "Тестовый проект"
    payload = {
        "title": new_project_name,
        "users": {
            "89bb33c3-f17d-40b6-b78e-02d2f834ea30": "admin"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    response = requests.post(
        f"{base_url}/projects",
        headers=headers,
        json=payload
    )

    assert response.status_code == 201, f"Ошибка создания проекта: ожидали статус 201, получили {response.status_code}"

 #негативный тест
def test_create_project_unauthorized():
    new_project_name = "Тестовый проект"
    payload = {
        "title": new_project_name,
        "users": {
            "89bb33c3-f17d-40b6-b78e-02d2f834ea30": "admin"
        }
    }

    headers = {
        "Content-Type": "application/json"
    } 

    response = requests.post(
        f"{base_url}/projects",
        headers=headers,
        json=payload
    )

    assert response.status_code == 401, f"Ошибочный статус: ожидали 401, получили {response.status_code}"

#позитивный тест
def test_update_project():
    project_id = "6d611f39-fcd1-40a0-91c6-bd704d92152c"

    update_payload = {
        "deleted": True,
        "title": "Обновленный проект",
        "users": {
            "89bb33c3-f17d-40b6-b78e-02d2f834ea30": "admin"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.put(f"{base_url}/projects/{project_id}", headers=headers, json=update_payload)

    assert response.status_code == 200, f"Ошибка обновления проекта: ожидали статус 200, получили {response.status_code}"

#негативный тест
def test_update_none_project():
    project_id = "NONE_PROJECT_ID"

    update_payload = {
        "deleted": True,
        "title": "Обновленный проект",
        "users": {
            "89bb33c3-f17d-40b6-b78e-02d2f834ea30": "admin"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.put(f"{base_url}/projects/{project_id}", headers=headers, json=update_payload)

    assert response.status_code == 404, f"Ошибка обновления несуществующего проекта: ожидали статус 404, получили {response.status_code}"

#позитивный тест
def test_get_project():
    
    project_id = "6d611f39-fcd1-40a0-91c6-bd704d92152c"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)

    assert response.status_code == 200, f"Ошибка получения проекта: ожидали статус 200, получили {response.status_code}"

    project_data = response.json()
    assert project_data["id"] == project_id, f"Полученный ID проекта не совпадает с запрошенным ({project_id})"

#негативный тест
def test_get_nonexistent_project():
    
    project_id = "NON_EXISTING_PROJECT_ID"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.get(f"{base_url}/projects/{project_id}", headers=headers)

    assert response.status_code == 404, f"Ошибка получения несуществующего проекта: ожидали статус 404, получили {response.status_code}"
