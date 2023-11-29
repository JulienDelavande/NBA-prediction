# Analyse des données


## Analyse de forme

- varaible cible: `TARGET_5Yrs`
- lignes et colonnes: 1340, 21
- type de variables: categorielles: 1, numeriques: 20
    (on supprimera la variable catégoriel Names qui ne nous sera pas utile)
- valeurs manquantes: `3P%` contient 11 NAN qui correspondent aux joueurs n'ayant pas marqués de 3 points 
    (on pourra les remplacer par 0)
- distribution de la target: 1.0=0.620149, 0.0=0.379851 
    (on a une distribution assez équilibrée, mais un rééquilabrage sera peut etre nécessaire)
- duplication de lignes: 12 lignes dupliquées, des joueurs ayant les mêmes noms ont été relevés mais pas les mêmes stats
    (on supprimera les lignes dupliquées)


## Analyse de fond

signification des variables:
    - `Name`: nom du joueur
    - `GP`: nombre de matchs joués
    - `MIN`: nombre de minutes jouées
    - `PTS`: nombre de points marqués
    - `FGM`: nombre de tirs marqués
    - `FGA`: nombre de tirs tentés
    - `FG%`: pourcentage de tirs marqués
    - `3P Made`: nombre de tirs à 3 points marqués
    - `3PA`: nombre de tirs à 3 points tentés
    - `3P%`: pourcentage de tirs à 3 points marqués
    - `FTM`: nombre de lancers francs marqués
    - `FTA`: nombre de lancers francs tentés
    - `FT%`: pourcentage de lancers francs marqués
    - `OREB`: nombre de rebonds offensifs
    - `DREB`: nombre de rebonds défensifs
    - `REB`: nombre de rebonds
    - `AST`: nombre de passes décisives
    - `STL`: nombre d'interceptions
    - `BLK`: nombre de contres
    - `TOV`: nombre de pertes de balle
    - `TARGET_5Yrs`: variable cible, 1 si le joueur a joué plus de 5 ans en NBA, 0 sinon
On remarque que certaines variables sont des produits d'autres variables (`FG%` = `FGM`/`FGA`, `3P%` = `3P Made`/`3PA`, `FT%` = `FTM`/`FTA`) et que d'autres sont des sommes de variables (`REB` = `OREB` + `DREB`).
