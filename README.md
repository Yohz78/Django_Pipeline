## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Yohz78/Projet_13.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Cette application fait aujourd'hui l'objet d'une pipeline CI/CD par l'utilisation de CircleCI, docker et heroku. Sentry est également actif et permet la surveillance de l'application.
Lors d'un commit github sur la branche main, la pipiline s'exécute. CircleCI execute alors les tests et le linting. Si ceux-ci sont effectués avec succès, la conteneurisation sur docker débute.
Une fois celle-ci correctement effectuée, le déploiement sur Heroku s'execute et Sentry est mis en place pour le monitoring de l'application.

Afin que l'ensemble du process s'effectue, toutes les étapes doivent être effectuées avec succès tel que décrit dans le workflow du fichier config.yml de CircleCI.

#### Prérequis

- Un compte CircleCI
- Un compte Dockerhub (avec un dépôt)
- Un compte Heroku (avec une application)
- Un compte Sentry (avec un projet)

### Mise en place

Tout d'abord, clonez le dépôt Github. Après cela, rendez-vous sur votre compte CircleCI, cliquez sur le bouton "Ajoutez un projet" et suivez les instructions afin de lier votre nouveau dépôt à CircleCI. N'acceptez pas que CircleCI génère automatiquement un fichier config.yml pour vous (vous en avez déjà un).

Vous devez en premier lieu clonez le répertoire github. Une fois cela fait, rendez vous sur votre compte CircleCI. Ajoutez un projet et liez le à votre dépot.
Votre projet contenant déjà un fichier config.yml, refusez l'option par défaut de génèse automatique d'un fichier de config.yml proposée par CircleCI.

Vous avez maintenant lié votre dépot github à CircleCI.

Pour ajouter docker à la pipeline, vous devez lier le dépot à votre compte et à un dépot dockerhub. Dans le fichier .circleci/config.yml, remplacez "yohz/oc_lettings" par le nom de votre dépot docker. Remplacez "oc-lettings-7892" par le nom de votre application heroku.

Vous allez ensuite devoir paramètrer vos variables d'environnement. Dans les settings de votre projet CircleCI, rajoutez les variables d'environnement suivantes :

- DOCKER_USER (votre nom d'utilisateur Docker),
- DOCKER_PASS (le mot de passe correspondant),
- HEROKU_TOKEN (le token associé à votre application Heroku, trouvable dans les paramètres de l'application"),
- SENTRY_AUTH_TOKEN (le token associé à votre compte Sentry),
- SENTRY_DNS (le DNS de votre projet Sentry),
- SENTRY_ORG et SENTRY_PROJECT (les noms de votre organisation et de votre project Sentry).

**Votre dépôt Github est maintenant lié à votre propre pipeline CircleCI.** Nous allons maintenant le lier à votre compte Docker.

Rendez-vous dans le fichier ".circleci/config.yml" et remplacez "lgarrigoux/oc_lettings" par le nom de votre dépôt DockerHub, puis "oc-lettings-9" par le nom de votre application Heroku.

Rendez-vous également dans les paramètres de votre application CircleCI et ajoutez les variables d'environnement suivantes :

- DOCKER_USER : Username Docker
- DOCKER_PASSWORD : Password Docker
- HEROKU_API_KEY : La clée associée à votre application Heroku
- HEROKU_APP_NAME : le nom de votre application Heroku
- SENTRY_AUTH_TOKEN : Le token d'identification de votre projet Sentry
- SENTRY_ORG : Le nom de votre organisation Sentry
- SENTRY_PROJECT : Le nom de votre projet Sentry

Vous avez maintenant mis en place une pipeline CI/CD complète.

Vous pouvez valider le déploiement en accédant à l'url de votre application Heroku et en utilisant /sentry-debug pour vérifier que votre release Sentry surveille bien l'application Heroku.
