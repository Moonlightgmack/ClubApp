https://github.com/Moonlightgmack/ClubApp.git

A
Profil utilisateur:
  Admin: gere tout les clubs et ses adhesion
  Utilisateur: consulter les clubs, s'inscrire et gere sa prope adhesion a un club
B
Responsable de club
1.En tant que responsable, je veux créer un club afin de permettre aux étudiants de découvrir et de rejoindre de nouvelles associations.
2.En tant que responsable, je veux consulter la liste des clubs afin d'avoir une vue d'ensemble des associations existantes.
3.En tant que responsable, je veux modifier les informations d'un club afin de maintenir ses informations à jour.
4.En tant que responsable, je veux supprimer un club afin de retirer les associations qui ne sont plus actives.
5.En tant que responsable, je veux consulter la liste des adhésions d'un club afin de connaître ses membres.
Utilisateur
1.En tant qu'étudiant, je veux consulter la liste des clubs disponibles afin de découvrir les associations auxquelles je peux participer.
2.En tant qu'étudiant, je veux consulter les détails d'un club afin de connaître ses activités, sa description et sa capacité maximale.
3.En tant qu'étudiant, je veux adhérer à un club afin de participer à ses activités.
4.En tant qu'étudiant, je veux consulter la liste de mes adhésions afin de connaître les clubs auxquels j'appartiens.
5.En tant qu'étudiant, je veux quitter un club afin de ne plus être considéré comme membre de cette association.
6.En tant qu'étudiant, je veux connaître le nombre de places disponibles dans un club afin de savoir s'il est encore possible de le rejoindre.

C


D:
## Arborescence des pages
| Adresse | Accès | Contenu |
|---|---|---|
| `/` | public | Liste des clubs, champ de recherche |
| `/clubs/{id}` | public | Détail, membres, bouton « Adhérer » |
| `/clubs/nouveau` | connecté | Formulaire de création |
| `/clubs/{id}/modifier` | créateur | Formulaire de modification, bouton supprimer |
| `/connexion`, `/inscription` | public | Formulaires |
| `/deconnexion` (POST) | connecté | Fin de session, redirection vers `/` |
| `/mes-adhesions` | connecté | Mes clubs (3 au plus) |