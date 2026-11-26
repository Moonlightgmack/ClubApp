"""Données de la séance 1, écrites en dur dans le code.

C'est volontaire : aujourd'hui on se concentre sur HTTP, HTML et CSS.
La séance 2 remplacera cette liste par une vraie couche métier, et la
séance 3 par une base de données.
"""
from datetime import datetime, timedelta

_aujourdhui = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

CLUBS = [
    {
        "id": 1,
        "nom": "club de programmation",
        "description": "Club ou ont apprend a coder en java,python,c,html,css et javascript.",
        "capacite": 25,
    },
    {
        "id": 2,
        "nom": "club de basket",
        "description": "Club ou ont apprend jouer au basket ball.",
        "capacite": 20,
    },
    {
        "id": 3,
        "nom": "club de  Football",
        "description": "Club ou ont apprend jouer au  football au niveau professionel.",
        "capacite": 45,
    },
    # {
    #     "id": 4,
    #     "nom": "club de  Trading",
    #     "description": "Club ou ont apprend a trader comme des professionnel avec different strategies",
    #     "capacite": 15,
    # },
]


def trouver_club(club_id: int) -> dict | None:
    for club in CLUBS:
        if club["id"] == club_id:
            return club
    return None
