# kalissssmarceau

Outil Python en ligne de commande pour regrouper des tests système et des fonctions d'automatisation sur Kali Linux.

> Utilise cet outil uniquement sur tes propres appareils, tes propres projets et tes environnements de laboratoire autorisés.

## Prérequis

- Kali Linux / Linux recommandé
- Python 3
- Git

Vérification :

```bash
python3 --version
git --version
```

## Installation sur Kali Linux

```bash
git clone https://github.com/alexmarceauprevost812-source/kalissssmarceau.git
cd kalissssmarceau
```

Aucune commande `npm install` n'est nécessaire : ce projet est en Python et les fichiers principaux utilisent la bibliothèque standard.

## Lancer l'outil principal

```bash
python3 kali_tools_automation.py
```

## Lancer les tests système

```bash
python3 test_kali.py
```

## Autres scripts du dépôt

- `kali_tools_automation.py` : menu principal.
- `test_kali.py` : tests système locaux.
- `install_kali_tools.py` : script expérimental d'installation; certaines commandes sont spécifiques à Linux et doivent être revues avant utilisation.
- `kali_termus.py` : prototype de menu terminal.
- `conversation_manager.py` : prototype de conversation; ce fichier contient encore du code expérimental à corriger.
- `index.html` : interface HTML/prototype.

## PowerShell / Windows

PowerShell peut servir à cloner et ouvrir le projet :

```powershell
git clone https://github.com/alexmarceauprevost812-source/kalissssmarceau.git
cd .\kalissssmarceau
```

Les scripts contiennent toutefois plusieurs commandes Linux (`df`, `apt-get`, etc.). Pour les exécuter correctement, utilise Kali Linux ou un environnement Linux compatible plutôt que de considérer le projet comme entièrement compatible Windows.

## Mise à jour du projet

Depuis le dossier du projet :

```bash
git pull origin main
```

## Structure

```text
kalissssmarceau/
├── README.md
├── kali_tools_automation.py
├── test_kali.py
├── install_kali_tools.py
├── install_kali_tools.sh
├── kali_termus.py
├── conversation_manager.py
├── cookie_manager.py
├── index.html
└── cookies.txt
```

## Démarrage rapide

```bash
git clone https://github.com/alexmarceauprevost812-source/kalissssmarceau.git
cd kalissssmarceau
python3 kali_tools_automation.py
```
