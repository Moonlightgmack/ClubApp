https://github.com/Moonlightgmack/ClubApp.git

A
## Profils d'utilisateurs
- **Visiteur** : consulte la liste et le détail des clubs, crée un compte.
- **Étudiant connecté** : adhère aux clubs (3 au plus), consulte ses adhésions.
- **Responsable de club** : étudiant connecté qui a créé un club ; il le modifie, le supprime et voit ses membres.

B
1. En tant que visiteur, je veux chercher un club par nom, afin de trouver une activité.
2. En tant que visiteur, je veux voir le détail d'un club (places restantes), afin de décider d'adhérer.
3. En tant que visiteur, je veux créer un compte et me connecter, afin de participer.
4. En tant qu'étudiant, je veux adhérer à un club, afin de participer à ses activités.
5. En tant qu'étudiant, je veux un message clair si le club est complet ou si j'ai déjà trois clubs, afin de comprendre le refus.
6. En tant que responsable, je veux créer un club avec un nombre maximal de membres, afin de maîtriser sa taille.
7. En tant que responsable, je veux modifier ou supprimer mon club, afin de garder ses informations à jour.
8. En tant que responsable, je veux voir mes membres, afin d'organiser les réunions.

C


D:
| Adresse | Méthode | Accès | Contenu de la page |
|---|---|---|---|
| `/` | GET | public | Page d'accueil « Clubs du campus » : nombre de clubs, champ de recherche (`/?q=photo`), une carte par club (nom, description, places restantes, bouton « Voir détail »). Si aucun club ne correspond : message « Aucun club trouvé ». |
| `/clubs/{id}` | GET | public | Détail d'un club : nom, description, places restantes sur le maximum, liste des membres, bouton « Rejoindre » (connecté et pas encore membre), boutons « Modifier » et « Supprimer » (créateur seulement), lien « Retour à l'accueil ». Club inexistant : page 404. |
| `/clubs/nouveau` | GET | connecté | Formulaire « Créer un club » : nom, description, capacité, boutons « Créer » et « Annuler ». Non connecté : redirection vers `/connexion`. |
| `/clubs` | POST | connecté | Traitement du formulaire de création. Données invalides : le formulaire est réaffiché avec les valeurs saisies et les erreurs en français. Succès : redirection vers `/clubs/{id}` (Post/Redirect/Get). |
| `/clubs/{id}/modifier` | GET | créateur | Formulaire de modification, prérempli. |
| `/clubs/{id}/modifier` | POST | créateur | Traitement de la modification, puis redirection vers `/clubs/{id}`. |
| `/clubs/{id}/supprimer` | POST | créateur | Suppression du club, puis redirection vers `/` avec un message de confirmation. |
| `/clubs/{id}/rejoindre` | POST | connecté | Adhésion au club. Puis redirection vers `/clubs/{id}` avec un message de succès ou d'erreur (club complet, déjà membre, trois clubs atteints). |
| `/mes-adhesions` | GET | connecté | Liste des clubs de l'étudiant (trois au plus). |
| `/inscription` | GET, POST | public | Formulaire de création de compte : nom, adresse e-mail, mot de passe. Succès : connexion automatique puis redirection vers `/`. |
| `/connexion` | GET, POST | public | Formulaire de connexion : adresse e-mail et mot de passe. Identifiants incorrects : message d'erreur. Succès : redirection vers `/`. |
| `/deconnexion` | POST | connecté | Fin de la session, redirection vers `/`. |


## Routes de l'API

|Méthode | Chemin      | Rôle            | Codes de statut |
|--------|-------------|-----------------|--------------------|
| GET    | `/api/clubs` | Lister les clubs ; `?q=` filtre par nom | 200 |
| GET    | `/api/clubs/{id}` | Lire le détail d'un club | 200, 404 |
| POST   | `/api/clubs`      | Créer un club (en-tête `Location`) | 201, 409 (nom déjà pris), 422 |
| POST   | `/api/clubs/{id}/adhesions` | Adhérer à un club | 201, 404, 409 (déjà membre, club complet, limite de trois clubs), 422 

## pour tester:
curl localhost:8000/api/clubs                                 # 200
curl -i localhost:8000/api/clubs/99                           # 404
curl -i -X POST localhost:8000/api/clubs -H "Content-Type: application/json" -d "{\"nom\":\"Club cinema\",\"capacite\":10}"                   # 201 + Location (club 5)
curl -i -X POST localhost:8000/api/clubs -H "Content-Type: application/json" -d "{\"nom\":\"Club cinema\",\"capacite\":10}"                  # 409 meme nom
curl -i -X POST localhost:8000/api/clubs/1/adhesions -H "Content-Type: application/json" -d "{\"id_utilisateur\":4}"                                  # 201
curl -i -X POST localhost:8000/api/clubs/1/adhesions -H "Content-Type: application/json" -d "{\"id_utilisateur\":4}"                                 # 409 déjà membre
curl -i -X POST localhost:8000/api/clubs/2/adhesions -H "Content-Type: application/json" -d "{\"id_utilisateur\":4}"                                   # 409 club complet
curl -i -X POST localhost:8000/api/clubs/5/adhesions -H "Content-Type: application/json" \
  -d '{"id_utilisateur":1}'                                   # 409 limite de trois clubs
## Tables
- **utilisateur** (id, nom, email UNIQUE, mot_de_passe_hash)
- **club** (id, nom UNIQUE, description, max_membres CHECK > 0, id_createur → utilisateur.id)
- **adhesion** (id_utilisateur → utilisateur.id, id_club → club.id, date_adhesion), clé primaire composée