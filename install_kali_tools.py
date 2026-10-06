#!/usr/bin/env python3

# GIBHUP REPO DU PROJET
print("https://github.com/kalilinux/kalilinux")

# Ajout pour Windows, Kali Linux et Termius
import platform

def get_terminal_command(tool):
    if platform.system() == 'Windows':
        return f'"{tool}"'
    elif platform.system() == 'Linux':
        return tool
    elif platform.system() == 'Darwin':
        return tool
    else:
        return tool

# install_kali_tools.py

import os
import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

def check_tool_installed(tool):
    try:
        subprocess.run(f"{get_terminal_command(tool)} --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_tool(tool):
    try:
        subprocess.run(f"{get_terminal_command(tool)} install -y {tool}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

def open_tool(tool):
    try:
        subprocess.run(f"{get_terminal_command(tool)}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

def install_kali_tools():
    tools = [
        "nmap",
        "metasploit-framework",
        "wireshark",
        "john",
        "hydra",
        "sqlmap",
        "burpsuite",
        "hashcat",
        "medusa",
        "nikto"
    ]
    for tool in tools:
        if not check_tool_installed(tool):
            print(f"Installing {tool}...")
            if install_tool(tool):
                print(f"{tool} installed successfully.")
            else:
                print(f"Failed to install {tool}.")
        else:
            print(f"{tool} is already installed.")

def open_kali_tools():
    tools = [
        "wireshark",
        "burpsuite"
    ]
    for tool in tools:
        if check_tool_installed(tool):
            print(f"Opening {tool}...")
            if open_tool(tool):
                print(f"{tool} opened successfully.")
            else:
                print(f"Failed to open {tool}.")
        else:
            print(f"{tool} is not installed.")

def main():
    print("Starting Kali Linux tools installation...")
    install_kali_tools()
    print("All Kali Linux tools installation completed.")
    print("Opening Kali Linux tools...")
    open_kali_tools()
    print("All Kali Linux tools opened.")

if __name__ == "__main__":
    main()