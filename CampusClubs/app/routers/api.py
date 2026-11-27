from fastapi import APIRouter, HTTPException, Response

from app import services
from app.schemas import (AdhesionCreation, AdhesionLecture, ClubCreation,
                         ClubLecture)

router = APIRouter(prefix="/api/clubs", tags=["clubs"])


@router.get("", response_model=list[ClubLecture])
def liste(q: str | None = None):
    return services.lister_clubs(q)


@router.get("/{id_club}", response_model=ClubLecture)
def detail(id_club: int):
    try:
        return services.obtenir_club(id_club)
    except services.ClubIntrouvable as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("", response_model=ClubLecture, status_code=201)
def creation(club: ClubCreation, response: Response):
    try:
        cree = services.creer_club(club.nom, club.description, club.capacite)
    except services.NomClubDejaPris as e:
        raise HTTPException(status_code=409, detail=str(e))
    response.headers["Location"] = f"/api/clubs/{cree['id']}"
    return cree


@router.post("/{id_club}/adhesions", response_model=AdhesionLecture,
             status_code=201)
def adhesion(id_club: int, demande: AdhesionCreation, response: Response):
    try:
        resultat = services.adherer(id_club, demande.id_utilisateur)
    except services.ClubIntrouvable as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (services.DejaMembre, services.ClubComplet,
            services.LimiteClubsAtteinte) as e:
        raise HTTPException(status_code=409, detail=str(e))
    response.headers["Location"] = f"/api/clubs/{id_club}"
    return resultat