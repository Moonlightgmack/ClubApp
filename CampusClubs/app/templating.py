"""Moteur de gabarits Jinja2 partagé par les routeurs de pages."""
from datetime import datetime

from fastapi.templating import Jinja2Templates

from app.config import NOM_APPLICATION

templates = Jinja2Templates(directory="app/templates")

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]


def date_fr(d: datetime) -> str:
    """Ex. : « vendredi 20 novembre 2026 à 10h00 » (indépendant de la locale du système)."""
    return f"{JOURS[d.weekday()]} {d.day} {MOIS[d.month - 1]} {d.year} à {d.hour}h{d.minute:02d}"


templates.env.filters["date_fr"] = date_fr
templates.env.globals["NOM_APPLICATION"] = NOM_APPLICATION
