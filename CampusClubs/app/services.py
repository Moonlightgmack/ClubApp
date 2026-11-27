from app import donnees

MAX_CLUBS_PAR_ETUDIANT = 3


# --- Exceptions of the domain ---
class ErreurClubs(Exception):
    """Root of all business errors."""


class ClubIntrouvable(ErreurClubs): pass
class NomClubDejaPris(ErreurClubs): pass
class DejaMembre(ErreurClubs): pass
class ClubComplet(ErreurClubs): pass
class LimiteClubsAtteinte(ErreurClubs): pass


# --- Internal helpers ---
def trouver_club(id_club: int) -> dict:
    for club in donnees.clubs:
        if club["id"] == id_club:
            return club
    raise ClubIntrouvable(f"Le club {id_club} n'existe pas.")


def nb_membres(id_club: int) -> int:
    return sum(1 for a in donnees.adhesions if a["id_club"] == id_club)


def lecture(club: dict) -> dict:
    n = nb_membres(club["id"])
    return {**club, "nb_membres": n, "places_restantes": club["capacite"] - n}


# --- Reading ---
def lister_clubs(q: str | None = None) -> list[dict]:
    clubs = donnees.clubs
    if q:
        clubs = [c for c in clubs if q.lower() in c["nom"].lower()]
    return [lecture(c) for c in clubs]


def obtenir_club(id_club: int) -> dict:
    return lecture(trouver_club(id_club))


# --- Creation ---
def creer_club(nom: str, description: str, capacite: int) -> dict:
    if any(c["nom"].lower() == nom.lower() for c in donnees.clubs):
        raise NomClubDejaPris(f"Un club nommé « {nom} » existe déjà.")
    nouvel_id = max((c["id"] for c in donnees.clubs), default=0) + 1
    club = {"id": nouvel_id, "nom": nom, "description": description,
            "capacite": capacite}
    donnees.clubs.append(club)
    return lecture(club)


# --- Business action: join a club ---
def adherer(id_club: int, id_utilisateur: int) -> dict:
    club = trouver_club(id_club)
    if any(a["id_utilisateur"] == id_utilisateur and a["id_club"] == id_club
           for a in donnees.adhesions):
        raise DejaMembre("Vous êtes déjà membre de ce club.")
    if nb_membres(id_club) >= club["capacite"]:
        raise ClubComplet(f"Le club « {club['nom']} » est complet.")
    nb_clubs = sum(1 for a in donnees.adhesions
                   if a["id_utilisateur"] == id_utilisateur)
    if nb_clubs >= MAX_CLUBS_PAR_ETUDIANT:
        raise LimiteClubsAtteinte(
            f"Un étudiant ne peut adhérer qu'à {MAX_CLUBS_PAR_ETUDIANT} clubs au maximum.")
    adhesion = {"id_utilisateur": id_utilisateur, "id_club": id_club}
    donnees.adhesions.append(adhesion)
    return adhesion