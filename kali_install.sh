#!/bin/bash

# Script d'installation de Kali Linux sur un environnement local

# Vérification des droits d'administrateur
if [ "$EUID" -ne 0 ]; then
  echo "Ce script doit être exécuté en tant qu'administrateur" 1>&2
  exit 1
fi

# Mise à jour du système
echo "Mise à jour du système..."
apt update && apt upgrade -y && apt dist-upgrade -y

# Installation des paquets nécessaires
echo "Installation des paquets nécessaires..."
apt install -y curl gnupg2 software-properties-common

# Ajout du dépôt Kali Linux
echo "Ajout du dépôt Kali Linux..."
curl -s https://archive.kali.org/archive-key.asc | apt-key add -
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | tee /etc/apt/sources.list.d/kali.list

# Mise à jour du système après l'ajout du dépôt Kali
echo "Mise à jour du système après l'ajout du dépôt Kali..."
apt update

# Installation de Kali Linux
echo "Installation de Kali Linux..."
apt install -y kali-linux-everything && apt autoremove -y && apt clean

# Nettoyage
echo "Nettoyage..."
apt clean

echo "Installation de Kali Linux terminée avec succès."
