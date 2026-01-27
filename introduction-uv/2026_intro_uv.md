# Introduction à **uv**

**`uv`** est un outil moderne et extrêmement rapide pour l’écosystème Python. Il unifie en un seul binaire :

* la gestion des versions de Python
* la création d’environnements virtuels
* l’installation et la résolution des dépendances
* la gestion de `pyproject.toml`, `uv.lock` et `requirements.txt`

Son objectif est de remplacer avantageusement :

* `pip`
* `venv`
* `pip-tools`
* et, dans de nombreux cas, `poetry`

tout en restant entièrement compatible avec les standards Python.

---

# 1. Pourquoi utiliser `uv` ?

Les outils classiques fonctionnent, mais présentent plusieurs limites :

* `pip` est lent
* `venv` est minimaliste
* `pip + pip-tools + venv` est fragmenté
* `poetry` peut être trop lourd pour des projets simples

`uv` apporte :

* une vitesse très élevée (écrit en Rust)
* une interface unifiée
* une résolution de dépendances fiable
* une forte reproductibilité via `uv.lock`
* une compatibilité native avec `pyproject.toml`

---

# 2. Installation de `uv`

Documentation officielle :
[https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

Vérification de l’installation :

```bash
uv --version
```

---

# 3. Initialiser un projet avec `uv`

## 3.1 Projet simple (scripts, recherche, notebooks)

```bash
uv init
```

### Structure créée par `uv init`

```text
.
├── .git
├── .gitignore
├── .python-version
├── .venv
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 3.2 Projet packagé (bibliothèque Python)

```bash
uv init --package
```

À utiliser si le projet est destiné à être :

* installé (`pip install .`)
* importé comme module
* publié (PyPI ou dépôt interne)

### Structure créée par `uv init --package`

```text
.
├── .git
├── .gitignore
├── .python-version
├── .venv
├── src/
│   └── mon_projet/
│       └── __init__.py
├── pyproject.toml
├── README.md
└── uv.lock

```

L’option `--package` :

* active un layout `src/`
* configure automatiquement le projet comme package installable
* est recommandée pour les bibliothèques et projets long terme

---

# 4. Rôle des fichiers clés

## `pyproject.toml` — source de vérité

Contient :

* les métadonnées du projet
* les dépendances déclarées
* les dépendances de développement
* la configuration des outils

Exemple minimal :

```toml
[project]
name = "mon-projet"
version = "0.1.0"
dependencies = []
```

---

## `uv.lock` — verrou de dépendances

Le fichier **`uv.lock`** est généré automatiquement par `uv`.

Il contient :

* les versions exactes des dépendances
* les hashes cryptographiques
* la résolution complète et reproductible

Il est équivalent, conceptuellement, à :

* `poetry.lock`
* `Pipfile.lock`

Le fichier `uv.lock` doit être versionné dans Git.

---

## `.python-version` -- version de Python

La version de Python est définie au niveau du projet via le fichier **`.python-version`**.

Ce fichier :

* indique la version de Python à utiliser
* est respecté par `uv venv` et `uv sync`
* garantit la reproductibilité entre machines

Il est recommandé de compléter avec :

```toml
[project]
requires-python = ">=3.XX,<3.XX"
```

Le fichier `.python-version` doit être versionné dans Git.

---

# 5. Ajouter des dépendances

```bash
uv add numpy
```

```bash
uv add numpy scipy matplotlib
```

Effets :

* mise à jour de `pyproject.toml`
* recalcul de `uv.lock`
* installation immédiate des dépendances

### Dépendances de développement

```bash
uv add --dev pytest black ruff
```

---

# 6. Synchroniser l’environnement

```bash
uv sync
```

`uv sync` :

* lit `pyproject.toml`
* utilise `uv.lock`
* installe exactement les versions verrouillées
* garantit la reproductibilité de l’environnement

Commande typique après un `git clone` ou en intégration continue.

---

# 7. Exporter les dépendances (`uv export`)

```bash
uv export --output-file=requirements.txt
```

Cette commande génère un fichier `requirements.txt` à partir de `uv.lock`.

Cas d’usage :

* environnements sans `uv`
* CI/CD legacy
* Docker
* compatibilité avec `pip`

Le couple `pyproject.toml` + `uv.lock` reste la source de vérité.
`requirements.txt` est un artefact dérivé.

---

# 8. Créer un environnement virtuel avec `uv`

```bash
uv venv
```

Cette commande crée un environnement virtuel dans :

```text
.venv/
```

Activation :

```bash
source .venv/bin/activate   # Linux / macOS
```

```powershell
.venv\Scripts\activate      # Windows
```

`uv venv` remplace `python -m venv .venv` tout en restant compatible avec l’écosystème Python standard.

---

# 9. Workflow recommandé

## Nouveau projet

```bash
uv init --package
uv add numpy scipy
uv sync
```

## Nouvelle machine ou CI

```bash
git clone ...
uv sync
```

L’environnement est recréé de manière identique.

---

# TL;DR 

```bash
uv init              # initialise un projet
uv init --package    # initialise un package Python
uv add               # ajoute des dépendances
uv sync              # synchronise depuis uv.lock
uv export            # génère requirements.txt
uv venv              # crée un environnement virtuel
```