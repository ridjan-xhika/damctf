## 📄 Description

> *"Simple Chessography substitution cipher"*

Ce challenge repose sur une technique de chiffrement originale : chaque caractère d’un message est disposé sur un échiquier, puis les pièces d’une vraie partie d’échecs (au format `.pgn`) sont utilisées pour effectuer des permutations de lettres, en suivant les mouvements des pièces.

L’auteur mentionne aussi une ouverture appelée *Orangutan Opening* comme clin d'œil, utilisée dans la partie fournie.

---

## 🧠 Méthodologie

### 🔍 Étapes de résolution

1. **Comprendre le chiffrement**
   Le message est placé **sur l’échiquier colonne par colonne**, de **haut en bas**, en partant de la **case a8 jusqu’à h1** (donc du coin haut gauche vers le coin bas droit pour le joueur blanc). Chaque mouvement d’échecs échange simplement deux caractères sur l’échiquier.

2. **Repérer le schéma de permutation**
   Le chiffrement ne modifie pas les lettres, mais uniquement leur **position** sur le plateau. Il suffit donc de **rejouer tous les mouvements à l’envers** pour retrouver le message original.

3. **Charger la partie d’échecs (`.pgn`)**
   Grâce à la bibliothèque `python-chess`, on peut charger le fichier `2025-05-09_Alice_vs_Bob.pgn` et extraire la séquence des coups joués.

4. **Appliquer les permutations inversées sur le message**
   On reconstruit l’échiquier à partir du fichier `message.txt`, puis on applique les **coups à l’envers** pour retrouver le message clair.

---


## 📦 Contenu des fichiers

* `message.txt` : texte brouillé visible, contenant des morceaux lisibles (`dam{`, `}`) mais dans le désordre.
* `2025-05-09_Alice_vs_Bob.pgn` : partie avec une ouverture "Orangutan" (d’où le nom du challenge).

---

## 🏁 Flag

Après avoir exécuté le script de déchiffrement, on obtient :

```
dam{ch3ss0graphy_1s_fun_but_did_y0u_f1nd_th3_or4ngutan?}
```

✅ **Flag** : `dam{ch3ss0graphy_1s_fun_but_did_y0u_f1nd_th3_or4ngutan?}`

---

## 🧠 Remarques

* La méthode est plus une **permutation de grille** qu’un vrai chiffrement par substitution.
* Le choix d’une ouverture "Orangutan" est un easter egg rigolo (et thématique).
* Le challenge est très difficile à résoudre à la main à cause du nombre élevé de coups. Le script est donc **presque obligatoire**, et bien aligné avec l’intention pédagogique de l’énigme.

---

## 🧰 Dépendances

Pour lancer le script :

```bash
pip install python-chess
python3 solve.py
```

---

## 📚 Références

* [python-chess (PyPI)](https://pypi.org/project/chess/)
* [Orangutan Opening – Wikipedia](https://en.wikipedia.org/wiki/Sokolsky_Opening)

---

