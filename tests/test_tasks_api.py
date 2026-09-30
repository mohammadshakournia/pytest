def test_create_task_returns_created_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Write API tests",
            "priority": "high",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 1,
        "title": "Write API tests",
        "priority": "high",
        "completed": False,
    }



def test_create_task_uses_medium_priority_by_default(client):
    response = client.post(
        "/tasks",
        json={"title": "Read documentation"},
    )

    assert response.status_code == 201
    assert response.json()["priority"] == "medium"


def test_list_tasks_returns_all_created_tasks(client):
    client.post(
        "/tasks",
        json={"title": "First task"},
    )

    client.post(
        "/tasks",
        json={
            "title": "Second task",
            "priority": "low",
        },
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["title"] == "First task"
    assert response.json()[1]["title"] == "Second task"


def test_get_task_returns_one_task(client):
    created_response = client.post(
        "/tasks",
        json={"title": "Find this task"},
    )

    created_task = created_response.json()

    response = client.get(f"/tasks/{created_task['id']}")

    assert response.status_code == 200
    assert response.json() == created_task



def test_get_missing_task_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_create_task_rejects_short_title(client):
    response = client.post(
        "/tasks",
        json={"title": "No"},
    )

    assert response.status_code == 422



def test_create_task_rejects_unknown_priority(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Invalid priority",
            "priority": "urgent",
        },
    )

    assert response.status_code == 422