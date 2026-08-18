# uni-main

A simple university course management system with a FastAPI backend and a React (Vite) frontend.  
The project is designed to work in **single-origin** mode in production (FastAPI serves the built frontend), while in development Vite proxies API calls to the backend to avoid CORS issues.

---

## Tech Stack

### Backend
- Python + **FastAPI**
- Pydantic (request validation)
- JWT-based authentication (via `SECRET_KEY`)
- Data persistence using JSON files under `uni-main/data/`

Backend dependencies are listed in `uni-main/requirements.txt` (e.g., `fastapi`, `uvicorn`, `pydantic`, `bcrypt`, `python-jose`).

### Frontend
- **React** + **Vite**
- Tailwind CSS
- Common UI libs used: `framer-motion`, `recharts`, `lucide-react` (see `uni-main/frontend/package.json`)

---

## Repository Structure (High Level)
```text
uni-main/
├─ main.py                  # FastAPI app entry point; mounts routers / serves frontend build
├─ routers/                 # API routers (auth, students, professors, courses, selection, access)
├─ services/                # business logic layer
├─ schemas/                 # Pydantic schemas
├─ data/                    # JSON data store (students, professors, courses)
├─ storage/                 # persistence helpers
└─ frontend/                # React/Vite frontend

---

## Running with Docker (Recommended)

### Prerequisites
- Docker
- Docker Compose

### Start
From the repository root:
bash
docker-compose up --build

### Environment variables
Set in `uni-main/docker-compose.yml` (around lines 10–14):
- `SECRET_KEY` (JWT signing key)
- `FRONTEND_ORIGIN` (frontend origin for CORS configuration)

Example:
env
SECRET_KEY=change-me-in-production
FRONTEND_ORIGIN=http://localhost:5173

### URLs
- Backend / App: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

> Docker Compose maps port `8000:8000` (see `uni-main/docker-compose.yml`, around lines 1–18).

---

## Running Locally (Development, no Docker)

### 1) Backend
From `uni-main/`:
bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

### 2) Frontend
From `uni-main/frontend/`:
bash
npm install
npm run dev

#### Dev Proxy (Vite)
In development, Vite runs on port `5173` and proxies API requests to the backend at `http://localhost:8000` (see `uni-main/frontend/vite.config.ts`, around lines 16–28).  
This helps avoid CORS issues during local development.

---

## Authentication & Client Behavior

- Frontend API base URL is set to an empty string `''`, meaning requests go to the same origin where the app is loaded (see `uni-main/frontend/src/api/client.ts`, line 9).
- Auth state (e.g., `token`, `role`, `sub`) is stored in `localStorage` and managed via React context (see `uni-main/frontend/src/context/AuthContext.tsx`, around lines 26–30).

### Example: Login endpoint
Frontend sends:
- `POST /auth/login` (see `uni-main/frontend/src/components/auth/LoginForm.tsx`, around lines 66–75)

Backend defines:
- router prefix `/auth`
- `POST /login` endpoint  
(see `uni-main/routers/auth.py`, prefix around line 10, endpoint around lines 31–40)

So the final endpoint is:
text
POST /auth/login

---

## Main API Route Prefixes

Routers are included in `uni-main/main.py` (around lines 21–26). Main prefixes:
- `/auth`
- `/students`
- `/professors`
- `/courses`
- `/selection`
- `/access`

---

## Data Storage

This project uses JSON files as a simple data store:
- `uni-main/data/students.json`
- `uni-main/data/professors.json`
- `uni-main/data/courses.json`

---

## Useful Tips (Debugging “Which endpoint does this button call?”)

Use Chrome DevTools:
1. Open DevTools (`F12`)
2. Go to **Network**
3. Clear existing requests
4. Click the button in the UI
5. Click the new request row
6. Check **Headers → Request URL** and **Request Method**
7. Use the **Initiator** column to jump to the TS/TSX file that triggered the request

---

## License
Add your license here (MIT / Apache-2.0 / etc).
