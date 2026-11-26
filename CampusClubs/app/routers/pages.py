"""Pages HTML rendues côté serveur (Jinja2), séance 1 : point de départ."""
from fastapi import APIRouter, Request

from app.donnees import CLUBS,trouver_club
from app.templating import templates

router = APIRouter()


@router.get("/api/sante")
def sante():
    # Une route qui renvoie du JSON : FastAPI convertit le dictionnaire.
    return {"statut": "ok"}


@router.get("/")
def accueil(request: Request):
    # TODO (fiche TD/TP, partie C) : trier les événements par date de début
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS})

@router.get("/clubs/{club_id}")
def detail_club(request:Request,club_id: int):
    club = trouver_club(club_id)
    return templates.TemplateResponse(request,"club.html",{"club":club})

@router.get("/club/creer")
def creer_club(request:Request):
    return templates.TemplateResponse(request,"club_creation_form.html")
# TODO (fiche TD/TP, partie D) : route GET /evenements/{evenement_id}
#   - utiliser trouver_evenement() du module app.donnees
#   - rendre evenement.html si l'événement existe
#   - sinon rendre 404.html avec le code de statut 404
