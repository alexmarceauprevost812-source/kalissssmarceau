Projet local créé avec TI-LEX CODEX.

## Installation

### Kali Linux

1. Ouvrez un terminal.
2. Exécutez les commandes suivantes :

```bash
sudo apt update
sudo apt install -y curl git
git clone https://github.com/your-repo/your-project.git
cd your-project
```

### Windows

1. Ouvrez un terminal (PowerShell ou Command Prompt).
2. Exécutez les commandes suivantes :

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-WebRequest -Uri "https://github.com/your-repo/your-project/archive/refs/heads/main.zip" -OutFile "project.zip"
Expand-Archive -Path "project.zip" -DestinationPath "."
cd your-project-main
```
