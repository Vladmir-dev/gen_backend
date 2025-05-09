import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@pytest.mark.asyncio
async def test_query_endpoint_success():
    mock_response = (
        "- Visa: Schengen visa required\n"
        "- Passport: Valid for 6 months beyond stay\n"
        "- Documents: Proof of funds, travel insurance\n"
        "- Advisories: Check for health alerts"
    )
    with patch("app.utils.llm.query_llm", return_value=mock_response) as mock_llm:
        response = client.post("/api/v1/query", json={"question": "What documents for Uganda to Germany?"})
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        assert "response" in response.json()
        # assert response.json()["response"] == mock_response
        # mock_llm.assert_called_once_with("What documents for Uganda to Germany?")

def test_query_endpoint_empty_question():
    response = client.post("/api/v1/query", json={"question": ""})
    assert response.status_code == 422  # Pydantic validation error

def test_query_endpoint_short_question():
    response = client.post("/api/v1/query", json={"question": "Hi"})
    assert response.status_code == 400
    assert "Question must be at least 5 characters long" in response.json()["detail"]
