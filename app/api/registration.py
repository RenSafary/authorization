from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse


router = APIRouter()

tmpl = Jinja2Templates(directory="./app/templates/")

@router.get("/sign-up/")
def reg_form(request: Request):
    return tmpl.TemplateResponse("registration.html", {"request": request})

@router.post("/sign-up/creating")
def user_create(
    login: str = Form(...),
    password: str = Form(...)
):
    print(login, password)
    return JSONResponse({
        "message": "account is created"
        })