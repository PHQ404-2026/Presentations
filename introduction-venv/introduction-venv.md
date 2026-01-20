# Environnements virtuels en Python

## 1. Qu’est-ce qu’un environnement virtuel ?

Un **environnement virtuel** est une installation Python isolée qui possède :

* Son propre interpréteur Python
* Ses propres bibliothèques installées
* Des versions de dépendances indépendantes

Cela permet d’éviter les conflits entre projets utilisant des versions différentes des mêmes packages.

---

## 2. Pourquoi utiliser des environnements virtuels ?

* Éviter les conflits de dépendances
* Rendre le code et les expériences reproductibles
* Tester et mettre à jour des bibliothèques sans risque
* Séparer proprement différents projets

C’est une bonne pratique essentielle en recherche et en développement.

---

## 3. Créer un environnement virtuel

### Avec `venv` (inclus dans Python ≥ 3.3)

```bash
python -m venv venv
```

Un dossier `venv/` est créé et contient l’environnement isolé.

---

## 4. Activer l’environnement

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

Une fois activé, le terminal affiche généralement :

```
(venv) $
```

---

## 5. Installer des packages

Lorsque l’environnement est activé, `pip` installe les bibliothèques **uniquement dans cet environnement** :

```bash
pip install numpy matplotlib
```

Lister les packages installés :

```bash
pip list
```

---

## 7. Sauvegarder les dépendances

Exporter les versions exactes des bibliothèques :

```bash
pip freeze > requirements.txt
```

Pour recréer l’environnement plus tard :

```bash
pip install -r requirements.txt
```

---

## 8. Désactiver l’environnement

```bash
deactivate
```

Vous revenez alors à l’interpréteur Python du système.

---

## 9. Alternatives courantes

* Environnements `conda`
* `uv` (gestion des dépendances et des projets)
* `poetry` (gestion des dépendances et des projets)
* `pipenv`

Pour les projets simples, `venv + pip` est simple et suffisant. Par contre, `uv` est fortement recommandé pour des projets plus complexes.

---

## Résumé (TL;DR)

```bash
python -m venv venv
source venv/bin/activate
pip install <packages>
deactivate
```

Les environnements virtuels permettent de garder des projets Python propres, isolés et reproductibles.
