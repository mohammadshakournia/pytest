import pytest
from fastapi.testclient import TestClient

from app import main



@pytest.fixture()
def client():
    main.tasks.clear()
    main.next_task_id = 1

    with TestClient(main.app) as test_client:
        yield test_client