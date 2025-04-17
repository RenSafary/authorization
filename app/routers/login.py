from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware



router = APIRouter()
tmpl = Jinja2Templates(directory="./app/templates")

@router.get("/form")
def form(
    request: Request
):
    return tmpl.TemplateResponse("login.html", {
        "request": request,
    })

@router.post("/login")
def login(
    request: Request,
    login: str = Form(...),
    password: str = Form(...)
):
    if login != "sad" or password != "sad":
        raise HTTPException(status_code=401, detail="Wrong login or password") 
    
    request.session["user"] = {
        "username": login,
        "logged_in": True
    }

    return JSONResponse({
        "message": "You are logged in"
    })