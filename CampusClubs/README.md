# AgendaCampus, point de départ (séance 1)

Application web de gestion des événements du campus, construite pas à pas
pendant le cours **Conception Web 1** (Licence 3 Informatique, Université
Adventiste Cosendai).

Ce dossier est volontairement incomplet : la fiche de TD/TP de la séance 1
vous guide pour le compléter (les `TODO` du code indiquent où intervenir).

## Lancer l'application SANS Docker (chemin par défaut)

Prérequis : Python 3.10 ou plus récent (3.11 à 3.14 pour l'installation hors ligne).

```bash
# 1. Se placer dans le dossier du projet
cd agendacampus

# 2. Créer et activer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate            # Windows (PowerShell ou cmd)
source .venv/bin/activate           # Linux / macOS

# 3. Installer les dépendances
pip install -r requirements.txt
#    sans Internet, avec le dossier wheelhouse fourni par l'enseignant :
pip install --no-index --find-links=../wheelhouse -r requirements.txt

# 4. Démarrer le serveur (rechargement automatique à chaque modification)
uvicorn app.main:app --reload
```

Ouvrir ensuite http://127.0.0.1:8000

## Lancer l'application AVEC Docker (option)

Prérequis : Docker Desktop (Windows/macOS) ou Docker Engine (Linux).

```bash
cd agendacampus
docker compose up --build
```

Ouvrir http://localhost:8000. Arrêt : `Ctrl+C`, puis `docker compose down`.

Les deux chemins font tourner **le même code** : seule la façon de
l'exécuter change.
