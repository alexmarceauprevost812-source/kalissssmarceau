# kalissssmarceau

Outil Python avec interface graphique pour Kali Linux.

> Utilise cet outil uniquement sur tes propres appareils, tes propres fichiers et des systèmes pour lesquels tu as une autorisation.

## Installation sur Kali Linux

Ouvre un terminal et exécute :

```bash
sudo apt update
sudo apt install -y git python3 python3-tk

cd ~
git clone https://github.com/alexmarceauprevost812-source/kalissssmarceau.git
cd kalissssmarceau
```

## Lancer l'outil

Depuis le dossier du projet :

```bash
cd ~/kalissssmarceau
python3 interface_choix.py
```

## Mettre l'outil à jour

```bash
cd ~/kalissssmarceau
git checkout main
git pull origin main
python3 interface_choix.py
```

## Si le dossier existe déjà

Ne refais pas `git clone`. Utilise simplement :

```bash
cd ~/kalissssmarceau
git checkout main
git pull origin main
python3 interface_choix.py
```

## Important

Le fichier `kali_install.sh` sert à installer/configurer des paquets Kali et n'est pas nécessaire pour lancer l'interface de cet outil.

Le point d'entrée graphique du projet est :

```text
interface_choix.py
```
