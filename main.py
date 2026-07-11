from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette import status
import os

from routers.students import router as students_router
from routers.professors import router as professors_router
from routers.courses import router as courses_router
from routers.selections import router as selections_router

from services.student_services import get_all_students
from services.professor_services import get_all_professors
from services.course_services import get_all_courses

app = FastAPI(title="University Management API")

os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(students_router)
app.include_router(professors_router)
app.include_router(courses_router)
app.include_router(selections_router)

# --- اصلاح شده: استفاده از request به عنوان آرگومان اول ---

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request, role: str = Query("student")):
    if role not in ["student", "professor", "admin"]:
        role = "student"
    return templates.TemplateResponse(request, "login.html", {"role": role})

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    role: str = Form(...)
):
    if role == "admin":
        if username == "@liflash11A" and password == "@liflash11A":
            return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)
        return HTMLResponse("کلمه عبور ادمین نادرست است.", status_code=400)

    elif role == "student":
        students = get_all_students()
        student = next((s for s in students if str(s.get("student_number")) == str(username) and str(s.get("national_id")) == str(password)), None)
        if not student:
            return HTMLResponse("شماره دانشجویی یا کد ملی اشتباه است.", status_code=400)
        return RedirectResponse(url=f"/student/dashboard/{username}", status_code=status.HTTP_303_SEE_OTHER)

    elif role == "professor":
        professors = get_all_professors()
        prof = next((p for p in professors if str(p.get("professor_code")) == str(username) and str(p.get("national_id")) == str(password)), None)
        if not prof:
            return HTMLResponse("کد استاد یا کد ملی اشتباه است.", status_code=400)
        return RedirectResponse(url=f"/professor/dashboard/{username}", status_code=status.HTTP_303_SEE_OTHER)

    return HTMLResponse("نقش کاربری نامعتبر است.", status_code=400)

@app.get("/student/dashboard/{student_num}", response_class=HTMLResponse)
async def student_dashboard(request: Request, student_num: str):
    students = get_all_students()
    student = next((s for s in students if str(s.get("student_number")) == str(student_num)), None)
    if not student:
        return RedirectResponse(url="/?role=student")

    all_courses = get_all_courses()
    professors = get_all_professors()
    selected_courses = student.get("selected_courses", [])
    available_courses = [c for c in all_courses if c["course_code"] not in selected_courses]

    professor_map = {p["professor_code"]: f"{p.get('first_name', '')} {p.get('last_name', '')}".strip() for p in professors}
    for course in available_courses:
        course["professor_name"] = professor_map.get(course["professor_code"], "نامشخص")

    return templates.TemplateResponse(request, "student_dash.html", {"student": student, "available_courses": available_courses})

@app.get("/student/info/{student_num}", response_class=HTMLResponse)
async def student_info(request: Request, student_num: str):
    students = get_all_students()
    student = next((s for s in students if str(s.get("student_number")) == str(student_num)), None)
    if not student:
        return HTMLResponse("دانشجو پیدا نشد", status_code=404)

    all_courses = get_all_courses()
    selected_codes = student.get("selected_courses", [])
    enrolled_courses = [c for c in all_courses if c["course_code"] in selected_codes]

    for course in enrolled_courses:
        grades_dict = course.get("grades", {})
        course["grade"] = grades_dict.get(student_num, None)

    return templates.TemplateResponse(request, "info.html", {"student": student, "enrolled_courses": enrolled_courses})

@app.get("/professor/dashboard/{prof_code}", response_class=HTMLResponse)
async def professor_dashboard(request: Request, prof_code: str):
    professors = get_all_professors()
    prof = next((p for p in professors if str(p.get("professor_code")) == str(prof_code)), None)
    if not prof:
        return RedirectResponse(url="/?role=professor")

    all_courses = get_all_courses()
    courses = [c for c in all_courses if str(c.get("professor_code")) == str(prof_code)]

    return templates.TemplateResponse(request, "professor_dash.html", {"professor": prof, "courses": courses})
