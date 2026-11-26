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
## Arborescence des pages
| Adresse | Accès | Contenu |
|---|---|---|
| `/` | public | Liste des clubs, champ de recherche |
| `/clubs/{club_id}` | public | Détail, membres, bouton « Adhérer » |
| `/clubs/nouveau` | connecté | Formulaire de création |
| `/clubs/{club_id}/modifier` | créateur | Formulaire de modification, bouton supprimer |
| `/connexion`, `/inscription` | public | Formulaires |
| `/deconnexion` (POST) | connecté | Fin de session, redirection vers `/` |
| `/mes-adhesions` | connecté | Mes clubs (3 au plus) |

## Routes de l'API
| Méthode | Chemin | Rôle | Codes |
|---|---|---|---|
| GET | `/api/clubs?q=` | Lister, filtrer par nom | 200 |
| GET | `/api/clubs/{id}` | Détail | 200, 404 |
| POST | `/api/clubs` | Créer (+ en-tête Location) | 201, 401, 409, 422 |
| PUT | `/api/clubs/{id}` | Modifier | 200, 401, 403, 404, 409, 422 |
| DELETE | `/api/clubs/{id}` | Supprimer | 204, 401, 403, 404 |
| POST | `/api/clubs/{id}/adhesions` | Adhérer (identité prise dans la session) | 201, 401, 404, 409 |

## Tables
- **utilisateur** (id, nom, email UNIQUE, mot_de_passe_hash)
- **club** (id, nom UNIQUE, description, max_membres CHECK > 0, id_createur → utilisateur.id)
- **adhesion** (id_utilisateur → utilisateur.id, id_club → club.id, date_adhesion), clé primaire composée