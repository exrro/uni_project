# 🎓 University Management System

<div align="center">

### A Full-Stack University Management System built with FastAPI

**REST API • Server-Side UI • OOP • Pydantic • JSON Storage • Docker**

<br>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge\&logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge\&logo=pydantic\&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge\&logo=jinja)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-000000?style=for-the-badge\&logo=linux)

</div>

---

## 📌 Overview

**University Management System** is a full-stack academic management application built with **Python and FastAPI**.

The system provides both a RESTful API and a server-rendered web interface for managing university entities such as:

* 👨‍🎓 Students
* 👨‍🏫 Professors
* 📚 Courses
* 📝 Course selections
* 📊 Student grades

The application follows a modular architecture that separates:

* API routing
* Business logic
* Data models
* Request validation
* Data persistence
* Presentation

The project was designed as a practical demonstration of building a structured backend application with FastAPI while maintaining a clean separation of responsibilities.

---

# ✨ Features

## 👨‍🎓 Student Management

Administrators can manage student records including:

* National ID
* First name
* Last name
* Student number
* Major
* Selected courses

Supported operations:

* Create student
* Retrieve all students
* Retrieve a student by student number
* Update student information
* Delete student

The system also prevents duplicate student numbers and duplicate national IDs.

---

## 👨‍🏫 Professor Management

Professor records can be created and managed through the API.

Each professor contains:

* National ID
* First name
* Last name
* Professor code
* Department
* Assigned courses

Supported operations:

* Create professor
* Retrieve professors
* Retrieve professor by code
* Update professor
* Delete professor

When a professor is deleted, courses assigned to that professor are automatically updated.

---

## 📚 Course Management

Courses contain:

* Course code
* Course title
* Number of units
* Assigned professor
* Enrolled students

Supported operations:

* Create course
* Retrieve courses
* Retrieve course by code
* Update course
* Delete course

Course units are validated using Pydantic constraints.

Valid range:

```text
1 → 6 units
```

The system also maintains relationships between courses and professors.

---

# 📝 Course Selection System

Students can select and drop courses through dedicated endpoints.

The selection system maintains relationships between:

```text
Student
   │
   ├── Selected Courses
   │
   └── Grades
```

and:

```text
Course
   │
   ├── Professor
   │
   └── Students
```

Supported operations:

* Select a course
* Drop a course
* List students enrolled in a course
* Assign or update student grades

The system also removes the corresponding relationship when a course is dropped.

---

# 📊 Grade Management

Professors can assign grades to students enrolled in their courses.

The system stores grades using the student's student number as the identifier.

Example relationship:

```text
Course
 └── grades
      ├── student_001 → 18.5
      ├── student_002 → 16.0
      └── student_003 → 19.25
```

Grades can be created or updated through the API.

---

# 🔐 Role-Based Login Flow

The web interface provides different login paths for:

* 👨‍🎓 Student
* 👨‍🏫 Professor
* 🛠️ Admin

After authentication, users are redirected to the appropriate interface.

### Student

Students are redirected to:

```text
/student/dashboard/{student_number}
```

### Professor

Professors are redirected to:

```text
/professor/dashboard/{professor_code}
```

### Admin

Administrators are redirected to the FastAPI API documentation.

---

# 🖥️ Web Interface

The application includes a server-rendered web interface powered by **Jinja2**.

The project contains dedicated templates for:

```text
templates/
│
├── base.html
├── index.html
├── login.html
├── info.html
├── student_dash.html
└── professor_dash.html
```

Static frontend assets are organized under:

```text
static/
│
├── css/
│   └── app.css
│
└── js/
    └── app.js
```

This allows the project to provide a user-facing interface in addition to its REST API.

---

# 🏗️ Architecture

The application follows a modular layered architecture:

```text
                    ┌─────────────────────┐
                    │      Web Client     │
                    │  Jinja2 / HTML / JS │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │       Routers       │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │   Students  │  │ Professors  │  │   Courses   │
       │   Router    │  │   Router    │  │   Router    │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │      Services       │
                    │   Business Logic    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Models        │
                    │   Domain Objects    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Data Storage     │
                    │       JSON          │
                    └─────────────────────┘
```

---

# 📁 Project Structure

```text
university-management-system/
│
├── main.py
│
├── data/
│   ├── __init__.py
│   ├── storage.py
│   ├── students.json
│   ├── professors.json
│   └── courses.json
│
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── student.py
│   ├── professor.py
│   └── course.py
│
├── routers/
│   ├── __init__.py
│   ├── students.py
│   ├── professors.py
│   ├── courses.py
│   └── selections.py
│
├── schemas/
│   ├── __init__.py
│   ├── student_schema.py
│   ├── professor_schema.py
│   └── course_schema.py
│
├── services/
│   ├── __init__.py
│   ├── student_services.py
│   ├── professor_services.py
│   ├── course_services.py
│   └── selection_services.py
│
├── static/
│   ├── css/
│   │   └── app.css
│   └── js/
│       └── app.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── info.html
│   ├── student_dash.html
│   └── professor_dash.html
│
├── requirements.txt
├── dockerfile
└── README.md
```

---

# 🧩 Core Components

## `main.py`

Application entry point.

Responsible for:

* Creating the FastAPI application
* Mounting static files
* Configuring Jinja2 templates
* Registering routers
* Handling authentication
* Serving dashboards
* Serving the main web interface

---

## `routers/`

Contains the HTTP API layer.

### `students.py`

Student CRUD endpoints.

### `professors.py`

Professor CRUD endpoints.

### `courses.py`

Course CRUD endpoints.

### `selections.py`

Course enrollment and grade endpoints.

---

## `services/`

Contains the application's business logic.

This layer handles operations such as:

* Creating entities
* Updating entities
* Deleting entities
* Validating relationships
* Maintaining course/student relationships
* Maintaining professor/course relationships
* Managing grades

Keeping this logic outside the routers makes the API layer cleaner and easier to maintain.

---

## `models/`

Contains domain models implemented using Python classes.

The project uses inheritance through:

```text
Person
 ├── Student
 └── Professor
```

This allows shared attributes such as:

* National ID
* First name
* Last name
* Full name

to be implemented in a common base class.

---

## `schemas/`

Contains Pydantic models responsible for validating incoming API data.

For example, student creation validates the national ID length:

```python
national_id: str = Field(..., min_length=10, max_length=10)
```

Course units are also validated:

```python
units: int = Field(..., ge=1, le=6)
```

---

## `data/`

Contains the persistence layer.

The current implementation uses JSON files:

```text
students.json
professors.json
courses.json
```

The storage module provides reusable functions for:

* Creating missing files
* Loading JSON data
* Saving JSON data

---

# 🌐 API Endpoints

## Students

### Get all students

```http
GET /students/
```

### Get student

```http
GET /students/{student_number}
```

### Create student

```http
POST /students/
```

### Update student

```http
PUT /students/{student_number}
```

### Delete student

```http
DELETE /students/{student_number}
```

---

# 👨‍🏫 Professors

### Get all professors

```http
GET /professors/
```

### Get professor

```http
GET /professors/{professor_code}
```

### Create professor

```http
POST /professors/
```

### Update professor

```http
PUT /professors/{professor_code}
```

### Delete professor

```http
DELETE /professors/{professor_code}
```

---

# 📚 Courses

### Get all courses

```http
GET /courses/
```

### Get course

```http
GET /courses/{course_code}
```

### Create course

```http
POST /courses/
```

### Update course

```http
PUT /courses/{course_code}
```

### Delete course

```http
DELETE /courses/{course_code}
```

---

# 📝 Selections & Grades

### Select course

```http
POST /selections/{student_number}/{course_code}
```

### Drop course

```http
DELETE /selections/{student_number}/{course_code}
```

### Get students enrolled in a course

```http
GET /selections/course/{course_code}
```

### Update student grade

```http
PUT /selections/grade
```

---

# 📖 Interactive API Documentation

FastAPI automatically generates interactive API documentation.

After running the application, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface allows API endpoints to be explored and tested directly from the browser.

---

# ⚙️ Requirements

The project uses:

```text
fastapi
uvicorn
pydantic
python-multipart
jinja2
```

Python 3.11+ is recommended.

---

# 🚀 Local Installation

## 1. Clone the repository

```bash
git clone https://github.com/exrro/university-management-system.git
```

## 2. Enter the project

```bash
cd university-management-system
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

The project includes a Docker configuration based on:

```text
python:3.11-slim
```

Build the image:

```bash
docker build -f dockerfile -t university-management-system .
```

Run the container:

```bash
docker run -p 8000:8000 university-management-system
```

Then access:

```text
http://127.0.0.1:8000
```

---

# 💾 Data Persistence

The current version intentionally uses JSON files instead of a relational database.

```text
data/
├── students.json
├── professors.json
└── courses.json
```

The storage layer automatically creates missing JSON files and safely loads valid list-based JSON data.

This makes the project easy to run locally without requiring additional database infrastructure.

---

# 🧠 Object-Oriented Design

The project demonstrates basic object-oriented domain modeling.

The hierarchy is:

```text
Person
│
├── Student
│
└── Professor
```

The `Person` class provides shared identity information, while specialized classes extend it with domain-specific properties.

### Student

```text
Person
 + student_number
 + major
 + selected_courses
```

### Professor

```text
Person
 + professor_code
 + department
 + courses
```

### Course

```text
Course
 + course_code
 + title
 + units
 + professor_code
 + students
```

---

# 🔄 Data Relationships

The system maintains relationships between the main entities.

```text
             ┌──────────────┐
             │  Professor   │
             └──────┬───────┘
                    │
                    │ teaches
                    ▼
             ┌──────────────┐
             │    Course    │
             └──────┬───────┘
                    │
                    │ enrolled
                    ▼
             ┌──────────────┐
             │   Student    │
             └──────────────┘
```

A course can have:

* One assigned professor
* Multiple students

A student can select:

* Multiple courses

Courses can also maintain:

* Student enrollment
* Student grades

---

# 🛡️ Validation & Error Handling

The application uses FastAPI and Pydantic validation together with HTTP exceptions.

Examples include:

* `404` when a student, professor or course does not exist
* `400` when attempting to create duplicate entities
* National ID validation
* Course unit validation
* Professor existence validation before course assignment

---

# 🔮 Future Improvements

The current architecture provides a strong foundation for further development.

Possible future improvements include:

* [ ] Replace JSON storage with PostgreSQL
* [ ] Add SQLAlchemy / SQLModel
* [ ] Implement JWT authentication
* [ ] Add password hashing
* [ ] Add role-based authorization
* [ ] Add database migrations
* [ ] Add automated tests with Pytest
* [ ] Add API versioning
* [ ] Add structured logging
* [ ] Add centralized exception handling
* [ ] Add Docker Compose
* [ ] Add CI/CD with GitHub Actions
* [ ] Add production deployment configuration
* [ ] Add pagination and filtering
* [ ] Add advanced academic reports
* [ ] Add GPA calculation
* [ ] Add semester management
* [ ] Add course capacity limits
* [ ] Add prerequisite courses
* [ ] Add database-backed authentication

---

# 📈 Project Evolution

The project can evolve from a local educational management application into a production-oriented academic platform.

```text
Current
   │
   ▼
FastAPI + JSON
   │
   ▼
PostgreSQL + ORM
   │
   ▼
JWT Authentication
   │
   ▼
Role-Based Authorization
   │
   ▼
Docker + CI/CD
   │
   ▼
Cloud Deployment
```

---

# 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* Python backend development
* FastAPI
* REST API design
* Pydantic validation
* Server-side rendering
* Jinja2 templates
* Object-oriented programming
* Layered application architecture
* CRUD operations
* Business logic separation
* Data persistence
* Relationship management
* Error handling
* Docker containerization

---

# 👨‍💻 Author

## exrro

Python Developer focused on:

**Artificial Intelligence • Backend Engineering • Automation • Web Scraping • Cybersecurity**

I enjoy building practical software systems and exploring the intersection of backend engineering, intelligent applications, automation and security.

GitHub:

https://github.com/exrro
---

<div align="center">

### Built with Python & FastAPI

**Design systems. Build APIs. Automate everything.**

</div>
