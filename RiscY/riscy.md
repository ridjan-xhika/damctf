## 📄 Description

> *Simple static rev challenge on an embedded RISCV device.*

Ce challenge nous plonge dans l’univers des systèmes embarqués, avec un binaire ELF compilé pour une architecture peu commune dans les CTFs : **RISCV 32-bit**, en environnement FreeRTOS.

---

## 🧠 Démarche de résolution

### 🔍 1. Identification de l’architecture

En lançant un simple `file` sur le binaire `esp_ota_client.elf`, on repère :

```bash
ELF 32-bit LSB executable, UCB RISC-V, version 1 (SYSV), statically linked
```

\=> Le binaire est bien un **exécutable statique RISCV 32-bit**.

---

### 🛠️ 2. Ouverture dans un décompilateur

J’ai utilisé **Ghidra**, qui supporte RISCV 32, pour charger le fichier.
À noter que d’autres outils comme Binary Ninja ou IDA Pro peuvent aussi convenir, mais Ghidra a l’avantage de gérer RISCV sans plugin externe.

---

### 📚 3. Recherche des points d’entrée

Grâce à la documentation de **FreeRTOS**, on sait que le point d’entrée applicatif est souvent une fonction nommée `app_main()`.

En naviguant vers `app_main` dans Ghidra, on peut suivre les appels successifs de fonctions.

---

### 🧩 4. Suivi logique jusqu’à la fonction `build_flag_task`

Dans `app_main`, un appel est fait vers une fonction que j’ai identifiée comme `build_flag_task`.
C’est dans cette fonction que le flag est reconstruit progressivement, à l’aide de plusieurs appels à `strcat`.

---

### 🧵 5. Reconstruction du flag

En inspectant les appels à `strcat`, et les valeurs successives ajoutées à la chaîne partagée , on peut retrouver le flag morceau par morceau.

Il commence comme attendu par `dam{` et les différentes concaténations permettent de reconstituer le flag final.

---

## 🧪 Éléments techniques notables

* Architecture : **RISC-V 32-bit**
* Plateforme : **FreeRTOS**
* Technique : **Reverse statique uniquement**
* Pas besoin d’émuler (même si c’est possible avec un QEMU forké, ce n’était pas nécessaire ici)
* Focus : Comprendre la construction de la chaîne `flag` via `strcat`

---

## 🏁 Flag

Flag reconstitué manuellement en suivant les chaînes dans `build_flag_task` :

```
dam{Fr33R705_15_C001_on_the_esp32c6}
```

*(flag exact non affiché ici par souci de spoil)*

---

## 🧠 Remarques

* Le challenge force à sortir des architectures x86/x64 habituelles, ce qui était rafraîchissant.
* Aucune émulation nécessaire : **toute la résolution peut se faire avec Ghidra** et un peu de patience.
* FreeRTOS est bien documenté, ce qui m’a permis d’identifier rapidement le `app_main`.

---

## ✅ TL;DR

* → ELF 32-bit RISCV
* → Décompilation avec Ghidra
* → Recherche de `app_main()`
* → Suivi logique jusqu’à `build_flag_task`
* → Analyse des `strcat` sur le buffer de flag
* → Flag extrait à la main, sans exécution dynamique

---
