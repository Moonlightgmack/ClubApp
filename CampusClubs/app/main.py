"""Point d'entrée de l'application AgendaCampus.

Lancement (depuis le dossier agendacampus) :
    uvicorn app.main:app --reload
puis ouvrir http://127.0.0.1:8000
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import NOM_APPLICATION
from app.routers import pages

app = FastAPI(title=NOM_APPLICATION)

# Les fichiers de /app/static (CSS, JS, images) sont servis tels quels sous /static
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(pages.router)
