"""Pages HTML rendues côté serveur avec Jinja2."""

from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse

from app.templating import templates
from app import services

router = APIRouter()


# ==========================================
# ACCUEIL : Liste des clubs
# ==========================================

@router.get("/")
def accueil(request: Request, q: str | None = None):

    clubs = services.lister_clubs(q)

    return templates.TemplateResponse(
        request,
        "index.html",
        {"clubs": clubs, "q": q}
    )

# CREATION : Afficher le formulaire

@router.get("/clubs/nouveau")
def creer_club(request: Request):

    return templates.TemplateResponse(
        request,
        "club_creation_form.html"
    )


# CREATION : Traiter le formulaire

@router.post("/clubs/nouveau")
def enregistrer_club(
    nom: str = Form(...),
    description: str = Form(...),
    capacite: int = Form(...)
):

    try:
        club = services.creer_club(nom, description, capacite)

    except services.NomClubDejaPris:

        return RedirectResponse(
            "/clubs/nouveau?erreur=nom_existe",
            status_code=status.HTTP_303_SEE_OTHER
        )

    return RedirectResponse(
        f"/clubs/{club['id']}",
        status_code=status.HTTP_303_SEE_OTHER
    )


# DETAIL : Afficher un club

@router.get("/clubs/{club_id}")
def detail_club(request: Request, club_id: int):

    try:
        club = services.obtenir_club(club_id)

    except services.ClubIntrouvable:

        return templates.TemplateResponse(
            request,
            "404.html",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return templates.TemplateResponse(
        request,
        "club.html",
        {"club": club}
    )


# ADHESION : Rejoindre un club

@router.post("/clubs/{club_id}/adhesions")
def adhesion(
    club_id: int,
    id_utilisateur: int = Form(...)
):

    try:
        services.adherer(club_id, id_utilisateur)

    except services.ClubIntrouvable:

        return RedirectResponse(
            "/?erreur=club_introuvable",
            status_code=status.HTTP_303_SEE_OTHER
        )

    except services.DejaMembre:

        return RedirectResponse(
            f"/clubs/{club_id}?erreur=deja_membre",
            status_code=status.HTTP_303_SEE_OTHER
        )

    except services.ClubComplet:

        return RedirectResponse(
            f"/clubs/{club_id}?erreur=club_complet",
            status_code=status.HTTP_303_SEE_OTHER
        )

    except services.LimiteClubsAtteinte:

        return RedirectResponse(
            f"/clubs/{club_id}?erreur=limite_atteinte",
            status_code=status.HTTP_303_SEE_OTHER
        )

    return RedirectResponse(
        f"/clubs/{club_id}",
        status_code=status.HTTP_303_SEE_OTHER
    )