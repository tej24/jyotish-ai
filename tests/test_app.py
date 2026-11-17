from fastapi.testclient import TestClient

from app.main import create_app

client = TestClient(create_app())


def test_healthz() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz_reports_version() -> None:
    body = client.get("/readyz").json()
    assert body["status"] == "ready"
    assert body["version"] == "0.1.0"


def test_index_renders_form() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Date of birth" in response.text
    assert "5 follow-up questions" in " ".join(response.text.split())


def test_security_headers_present() -> None:
    headers = client.get("/healthz").headers
    assert headers["X-Frame-Options"] == "DENY"
    assert "default-src 'self'" in headers["Content-Security-Policy"]
