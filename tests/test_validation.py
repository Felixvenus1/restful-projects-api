"""Validation error handling tests."""
import pytest
from fastapi.testclient import TestClient


class TestProjectNameValidation:
    """Tests for project name field validation."""
    def test_name_required(self, client: TestClient):
        """Test that name field is required."""
        response = client.post(
            "/projects",
            json={"description": "Missing name"},
        )
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        errors = data["detail"]
        assert any("name" in str(error).lower() for error in errors)

    def test_name_empty_string(self, client: TestClient):
        """Test that empty name string is rejected."""
        response = client.post(
            "/projects",
            json={"name": "", "description": "Empty name"},
        )
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data

    def test_name_too_long(self, client: TestClient):
        """Test that name exceeding max length is rejected."""
        long_name = "a" * 121  # Max is 120
        response = client.post(
            "/projects",
            json={"name": long_name},
        )
        assert response.status_code == 422

    def test_name_max_length_valid(self, client: TestClient):
        """Test that name at max length is accepted."""
        name = "a" * 120
        response = client.post(
            "/projects",
            json={"name": name},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == name


class TestProjectDescriptionValidation:
    """Tests for project description field validation."""
    
    def test_description_optional(self, client: TestClient):
        """Test that description is optional."""
        response = client.post(
            "/projects",
            json={"name": "Project"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["description"] is None


    def test_description_too_long(self, client: TestClient):
        """Test that description exceeding max length is rejected."""
        long_desc = "a" * 2001  # Max is 2000
        response = client.post(
            "/projects",
            json={"name": "Project", "description": long_desc},
        )
        assert response.status_code == 422

    def test_description_max_length_valid(self, client: TestClient):
        """Test that description at max length is accepted."""
        desc = "a" * 2000
        response = client.post(
            "/projects",
            json={"name": "Project", "description": desc},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["description"] == desc


class TestProjectStatusValidation:
    """Tests for project status field validation."""
    def test_status_default_value(self, client: TestClient):
        """Test that status defaults to 'planned'."""
        response = client.post(
            "/projects",
            json={"name": "Project"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["status"] == "planned"

    def test_status_valid_values(self, client: TestClient):
        """Test all valid status values."""
        valid_statuses = ["planned", "pending", "complete"]
        for status in valid_statuses:
            response = client.post(
                "/projects",
                json={"name": f"Project {status}", "status": status},
            )
            assert response.status_code == 201
            data = response.json()
            assert data["status"] == status

    def test_status_invalid_value(self, client: TestClient):
        """Test that invalid status value is rejected."""
        response = client.post(
            "/projects",
            json={"name": "Project", "status": "invalid_status"},
        )
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data

    def test_update_with_invalid_status(self, client: TestClient):
        """Test that invalid status in update is rejected."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "Project"},
        )
        project_id = create_response.json()["id"]

        # Try to update with invalid status
        response = client.put(
            f"/projects/{project_id}",
            json={"status": "invalid"},
        )
        assert response.status_code == 422


class TestUpdateValidation:
    """Tests for update request validation."""

    def test_update_name_too_long(self, client: TestClient):
        """Test that update with long name is rejected."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "Project"},
        )
        project_id = create_response.json()["id"]

        # Try to update with long name
        long_name = "a" * 121
        response = client.put(
            f"/projects/{project_id}",
            json={"name": long_name},
        )
        assert response.status_code == 422

    def test_update_description_too_long(self, client: TestClient):
        """Test that update with long description is rejected."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "Project"},
        )
        project_id = create_response.json()["id"]

        # Try to update with long description
        long_desc = "a" * 2001
        response = client.put(
            f"/projects/{project_id}",
            json={"description": long_desc},
        )
        assert response.status_code == 422

    def test_update_with_empty_json(self, client: TestClient):
        """Test that update with empty JSON body is allowed (no changes)."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "Original"},
        )
        project_id = create_response.json()["id"]

        # Update with empty body
        response = client.put(
            f"/projects/{project_id}",
            json={},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Original"


class TestInvalidJsonHandling:
    """Tests for handling invalid JSON inputs."""

    def test_missing_required_field(self, client: TestClient):
        """Test proper error when required field is missing."""
        response = client.post("/projects", json={})
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data

    def test_invalid_json_type(self, client: TestClient):
        """Test handling of wrong data types."""
        response = client.post(
            "/projects",
            json={"name": 123},  # name should be string
        )
        assert response.status_code == 422
