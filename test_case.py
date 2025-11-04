import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/agent/query"

@pytest.fixture(scope="session", autouse=True)
def check_server_running():
    """Ensure the FastAPI server is running before tests."""
    try:
        requests.get("http://127.0.0.1:8000/docs", timeout=3)
    except Exception:
        pytest.exit("❌ FastAPI server is not running. Start it using 'uvicorn main:app --reload'")

def test_calculator():
    payload = {"prompt": "calculate 10 + 5 * 2"}
    response = requests.post(BASE_URL, json=payload)
    data = response.json()
    assert "response" in data
    assert "result" in data["response"]
    assert data["response"]["result"] == 20
    print("Calculator test passed")

def test_memory_save():
    payload = {"prompt": "remember my name is Nagabharath"}
    response = requests.post(BASE_URL, json=payload)
    data = response.json()
    assert data["response"]["status"] == "saved"
    print("Memory save test passed")

def test_memory_recall():
    payload = {"prompt": "what is my name"}
    response = requests.post(BASE_URL, json=payload)
    data = response.json()
    assert "value" in data["response"]
    assert data["response"]["value"].lower() == "nagabharath"
    print("Memory recall test passed")

