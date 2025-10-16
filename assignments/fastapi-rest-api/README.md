# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. Students will gain hands-on experience with endpoints, request/response handling, and basic CRUD operations.

## 📝 Tasks

### 🛠️ FastAPI Project Setup

#### Description
Set up a new FastAPI project and run a simple web server.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main application file (e.g., `main.py`)
- Start the FastAPI server and verify it runs locally

### 🛠️ Create Basic Endpoints

#### Description
Implement basic GET and POST endpoints for a resource (e.g., items, books, or users).

#### Requirements
Completed program should:

- Define a data model using Pydantic
- Create a GET endpoint to list all resources
- Create a POST endpoint to add a new resource
- Return appropriate status codes and JSON responses

### 🛠️ Implement CRUD Operations

#### Description
Expand the API to support full CRUD (Create, Read, Update, Delete) operations for the resource.

#### Requirements
Completed program should:

- Add endpoints for retrieving, updating, and deleting a resource by ID
- Validate input and handle errors gracefully
- Test all endpoints using an API client (e.g., curl, httpie, or Swagger UI)

### 🛠️ Documentation and Testing

#### Description
Document the API and demonstrate how to test it.

#### Requirements
Completed program should:

- Use FastAPI's automatic docs (Swagger UI)
- Provide example requests and responses in the README
- Encourage students to test endpoints and explore the docs
