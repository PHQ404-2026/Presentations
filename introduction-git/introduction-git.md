# Introduction à **GitHub**

GitHub est une plateforme basée sur **Git** qui permet de :

* versionner du code
* collaborer à plusieurs
* partager et archiver des projets
* assurer la reproductibilité et la traçabilité du travail

C’est aujourd’hui un outil standard en recherche et en développement.

---

## 1. Git vs GitHub

* **Git** : outil local de gestion de versions
* **GitHub** : service en ligne qui héberge des dépôts Git et facilite la collaboration

On utilise Git sur sa machine, et GitHub comme serveur distant.

---

## 2. Créer un dépôt GitHub

1. Créer un compte sur GitHub
2. Cliquer sur **New repository**
3. Donner un nom au projet
4. Initialiser (ou non) avec un `README.md`

Le dépôt est alors accessible via une URL.

---

## 3. Connexion à GitHub: SSH vs HTTPS

* **SSH** (recommandé): Sécurisé, utilise des clés publiques/privées pour se connecter sans mot de passe.
* **HTTPS** : Utilise un **Personal Access Token (PAT)** comme mot de passe.

### Ajouter une clé SSH à GitHub :

```bash
ssh-keygen -t ed25519 -C "votre.email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Copier la clé publique dans GitHub **Settings > SSH and GPG keys**.

Test de la connexion SSH :

```bash
ssh -T git@github.com
```

### Utiliser HTTPS avec un token d’accès personnel :

1. Générer un token dans **Settings > Developer settings > Personal access tokens**
2. Lors du push/pull via HTTPS, utiliser votre username et le token comme mot de passe

```bash
git push https://username@github.com/UTILISATEUR/PROJET.git
```

---

## 4. Cloner un dépôt existant

Pour récupérer un projet GitHub existant sur votre machine :

```bash
# avec SSH
git clone git@github.com:UTILISATEUR/PROJET.git
# avec HTTPS
git clone https://github.com/UTILISATEUR/PROJET.git
cd PROJET
```

---

## 5. Workflow de base

Cycle typique de travail :

```bash
git status          # vérifier les changements

# ajouter les fichiers modifiés
 git add fichier.py

# enregistrer un commit
 git commit -m "Message clair"

# envoyer les changements sur GitHub
 git push

# récupérer les dernières modifications depuis GitHub
 git pull

# récupérer les changements sans fusion automatique
 git fetch

# fusionner une branche dans la branche actuelle
 git merge branche
```

Bonnes pratiques :

* commits fréquents
* messages descriptifs
* un commit = une idée

---

## 6. Branches

Créer une branche :

```bash
git checkout -b nouvelle-branche
```

Fusionner dans `main` :

```bash
git checkout main
git merge nouvelle-branche
```

Les branches permettent de travailler sans casser le code principal.

---

## 7. Fichiers importants

### `.gitignore`

Liste les fichiers à ne pas versionner (ex : `.venv/`, fichiers temporaires) :

```text
.venv/
__pycache__/
*.pyc
```

### `README.md`

Explique :

* le but du projet
* comment l’installer
* comment l’utiliser

---

## 8. GitHub en pratique pour un projet Python

Structure typique :

```text
projet/
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
└── notebooks/
```

---

## 11. À retenir

* GitHub est un standard pour le partage de code
* Il facilite la collaboration et la reproductibilité
* Même pour un projet solo, GitHub est très utile

---

## Résumé (TL;DR)

```bash
git clone git@github.com:UTILISATEUR/PROJET.git
cd PROJET
git add .
git commit -m "msg"
git push
git pull
git fetch
git merge branche
```

GitHub permet de garder un historique clair et partageable de vos projets, avec un workflow collaboratif efficace et sécurisé.