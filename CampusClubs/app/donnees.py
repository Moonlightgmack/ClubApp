"""Données de la séance 1, écrites en dur dans le code.

C'est volontaire : aujourd'hui on se concentre sur HTTP, HTML et CSS.
La séance 2 remplacera cette liste par une vraie couche métier, et la
séance 3 par une base de données.
"""
from datetime import datetime, timedelta

clubs = [
    {"id": 1, "nom": "Club photo", "description": "Sorties et ateliers photo", "capacite": 20},
    {"id": 2, "nom": "Club échecs", "description": "Tournois hebdomadaires", "capacite": 2},
    {"id": 3, "nom": "Club robotique", "description": "Projets de compétition", "capacite": 15},
    {"id": 4, "nom": "Club théâtre", "description": "Troupe et spectacles", "capacite": 25},
]

adhesions = [
    {"id_utilisateur": 1, "id_club": 1},
    {"id_utilisateur": 1, "id_club": 3},
    {"id_utilisateur": 1, "id_club": 4},   # user 1 already has three clubs
    {"id_utilisateur": 2, "id_club": 2},
    {"id_utilisateur": 3, "id_club": 2},   # club 2 is full (capacity 2)
]
