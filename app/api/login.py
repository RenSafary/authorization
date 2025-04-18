from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv


router = APIRouter()
tmpl = Jinja2Templates(directory="./app/templates")

load_dotenv()
api_key = os.environ.get("API_KEY")

@router.get("/form/{key}")
def form(
    request: Request,
    key: str,
):
    print(api_key)
    if key != api_key:
        return JSONResponse(
            {"error": "api key is invalid!"}
        )

    if "user" not in request.session:
        return tmpl.TemplateResponse("login.html", {"request": request})
    else: 
        return JSONResponse({
            "message": "You are logged in"
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