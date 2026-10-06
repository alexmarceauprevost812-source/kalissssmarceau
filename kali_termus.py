#!/usr/bin/env python3
# kali_termus.py

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
        subprocess.run(f"{tool} --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_tool(tool):
    try:
        subprocess.run(f"apt-get install -y {tool}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

def menu_item_3_add_target():
    print("Starting network test...")
    result = run_command("curl -I https://example.com")
    print("Network test result:")
    print(result)

def menu_item_4_execute_attacks():
    print("Starting disk space test...")
    result = run_command("du -sh /path/to/device")
    print("Disk space test result:")
    print(result)

def menu_item_5_security_results():
    print("Starting Python version test...")
    result = run_command("python3 --version")
    print("Python version test result:")
    print(result)

def menu_item_6_find_device_secrets():
    print("Starting Kali Linux tools installation...")
    if not check_tool_installed("kalissmarceau"):
        install_tool("kalissmarceau")
    print("Starting Kali Linux tools execution...")
    run_command("kalissmarceau")
    print("Kali Linux tools execution result:")
    print(run_command("kalissmarceau"))
    print("Starting top 10 Kali Linux tools test...")
    result = run_command("ls /usr/share/kali-linux-tools")
    print("Top 10 Kali Linux tools test result:")
    print(result)

def main():
    print("Welcome to Kali Termus!")
    print("1. Add target")
    print("2. Execute attacks")
    print("3. Security results")
    print("4. Find device secrets")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        menu_item_3_add_target()
    elif choice == "2":
        menu_item_4_execute_attacks()
    elif choice == "3":
        menu_item_5_security_results()
    elif choice == "4":
        menu_item_6_find_device_secrets()
    elif choice == "5":
        print("Exiting Kali Termus.")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()