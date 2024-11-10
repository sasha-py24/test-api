from config import app, templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from sqlalchemy.orm import Session
from db import get_db, Project


# дані якого типу ми передаємо, бо серевер вважає що всі дані ми повертаємо у форматі json


@app.get('/', response_class = HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):     # параметр щоб дістати щось з бд
    projects = db.query(Project).all()

    return templates.TemplateResponse('index.html', {'title': 'Projects', 'projects': projects, 'request': request})          # сервер  повертає значення у форматі json



