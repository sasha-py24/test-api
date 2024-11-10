from fastapi import FastAPI
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
# обєкт класу, де прописуємо шлях до папки бо програма не розуміє