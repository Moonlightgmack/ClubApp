"""Pages HTML rendues côté serveur (Jinja2), séance 1 : point de départ."""
from fastapi import APIRouter, Request,status

from app.donnees import CLUBS,trouver_club
from app.templating import templates

router = APIRouter()




@router.get("/")
def accueil(request: Request):
    # TODO (fiche TD/TP, partie C) : trier les événements par date de début
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS})


@router.get("/clubs/nouveau")
def creer_club(request:Request):
    return templates.TemplateResponse(request,"club_creation_form.html")

@router.get("/clubs/{club_id}")
def detail_club(request:Request,club_id: int):
    
    club = trouver_club(club_id)
    if club == None:
         return templates.TemplateResponse(request,"404.html",status_code=status.HTTP_404_NOT_FOUND)
    return templates.TemplateResponse(request,"club.html",{"club":club})
   


@router.put("/clubs/{club_id}/modifier")
def modifier():
      pass