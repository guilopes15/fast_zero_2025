import pytest
from fastapi.testclient import TestClient

from fast_zero_2025.app import app


@pytest.fixture
def client():
    return TestClient(app)
