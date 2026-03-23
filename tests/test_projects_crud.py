"""CRUD endpoint integration tests."""
import pytest
from fastapi.testclient import TestClient


class TestProjectCreation:
    """Tests for POST /projects endpoint."""

    def test_create_project_success(self, client: TestClient):
        """Test successful project creation."""
        response = client.post(
            "/projects",
            json={
                "name": "Test Project",
                "description": "A test project",
                "status": "planned",
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test Project"
        assert data["description"] == "A test project"
        assert data["status"] == "planned"
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data

    def test_create_project_minimal(self, client: TestClient):
        """Test project creation with only required fields."""
        response = client.post(
            "/projects",
            json={"name": "Minimal Project"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Minimal Project"
        assert data["description"] is None
        assert data["status"] == "planned"

    def test_create_project_with_custom_status(self, client: TestClient):
        """Test project creation with custom status."""
        response = client.post(
            "/projects",
            json={
                "name": "In Progress Project",
                "status": "pending",
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["status"] == "pending"


class TestProjectRetrieval:
    """Tests for GET /projects endpoints."""

    def test_get_all_projects_empty(self, client: TestClient):
        """Test retrieving projects when none exist."""
        response = client.get("/projects")
        assert response.status_code == 200
        data = response.json()
        assert data == []

    def test_get_all_projects(self, client: TestClient):
        """Test retrieving all projects."""
        # Create multiple projects
        for i in range(3):
            client.post(
                "/projects",
                json={"name": f"Project {i}", "status": "planned"},
            )

        response = client.get("/projects")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3
        assert all("id" in item for item in data)
        assert all("name" in item for item in data)

    def test_get_projects_by_status_filter(self, client: TestClient):
        """Test filtering projects by status."""
        # Create projects with different statuses
        client.post(
            "/projects",
            json={"name": "Planned 1", "status": "planned"},
        )
        client.post(
            "/projects",
            json={"name": "Pending 1", "status": "pending"},
        )
        client.post(
            "/projects",
            json={"name": "Planned 2", "status": "planned"},
        )

        response = client.get("/projects?status=planned")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert all(item["status"] == "planned" for item in data)

        response = client.get("/projects?status=pending")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["status"] == "pending"

    def test_get_project_by_id_success(self, client: TestClient):
        """Test retrieving a single project by ID."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "Test Project", "description": "Test desc"},
        )
        project_id = create_response.json()["id"]

        response = client.get(f"/projects/{project_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id
        assert data["name"] == "Test Project"
        assert data["description"] == "Test desc"

    def test_get_project_by_id_not_found(self, client: TestClient):
        """Test retrieving a non-existent project."""
        response = client.get("/projects/999")
        assert response.status_code == 404
        data = response.json()
        assert "not found" in data["detail"].lower()


class TestProjectUpdate:
    """Tests for PUT /projects/{id} endpoint."""

    def test_update_project_all_fields(self, client: TestClient):
        """Test updating all fields of a project."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={
                "name": "Original",
                "description": "Original desc",
                "status": "planned",
            },
        )
        project_id = create_response.json()["id"]

        # Update the project
        response = client.put(
            f"/projects/{project_id}",
            json={
                "name": "Updated",
                "description": "Updated desc",
                "status": "complete",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id
        assert data["name"] == "Updated"
        assert data["description"] == "Updated desc"
        assert data["status"] == "complete"

    def test_update_project_partial(self, client: TestClient):
        """Test partial update (only some fields)."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={
                "name": "Original",
                "description": "Original desc",
                "status": "planned",
            },
        )
        project_id = create_response.json()["id"]

        # Update only the name
        response = client.put(
            f"/projects/{project_id}",
            json={"name": "Name Updated"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Name Updated"
        assert data["description"] == "Original desc"  # Unchanged
        assert data["status"] == "planned"  # Unchanged

    def test_update_project_not_found(self, client: TestClient):
        """Test updating a non-existent project."""
        response = client.put(
            "/projects/999",
            json={"name": "Updated"},
        )
        assert response.status_code == 404

    def test_update_project_only_status(self, client: TestClient):
        """Test updating only the status field."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "Project", "status": "planned"},
        )
        project_id = create_response.json()["id"]

        response = client.put(
            f"/projects/{project_id}",
            json={"status": "pending"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "pending"
        assert data["name"] == "Project"


class TestProjectDeletion:
    """Tests for DELETE /projects/{id} endpoint."""

    def test_delete_project_success(self, client: TestClient):
        """Test successful project deletion."""
        # Create a project
        create_response = client.post(
            "/projects",
            json={"name": "To Delete"},
        )
        project_id = create_response.json()["id"]

        # Delete it
        response = client.delete(f"/projects/{project_id}")
        assert response.status_code == 204
        assert response.content == b""

        # Verify it's gone
        get_response = client.get(f"/projects/{project_id}")
        assert get_response.status_code == 404

    def test_delete_project_not_found(self, client: TestClient):
        """Test deleting a non-existent project."""
        response = client.delete("/projects/999")
        assert response.status_code == 404


class TestHealthCheck:
    """Tests for health check endpoint."""

    def test_health_check(self, client: TestClient):
        """Test the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
