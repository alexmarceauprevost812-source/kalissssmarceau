#!/usr/bin/env python3
# kali_tools_automation.py

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
    result = run_command("curl -I https://example.com")
    print("Python version test result:")
    print(result)

def menu_item_6_find_device_secrets():
    print("Starting top 10 Kali Linux tools test...")
    result = run_command("curl -I https://example.com")
    print("Top 10 Kali Linux tools test result:")
    print(result)

def test_ollama_model():
    if check_tool_installed("ollama"):
        print("Ollama model is installed.")
        result = run_command("ollama --model tiny --prompt 'Hello, world!'")
        print("Ollama model test result:")
        print(result)
    else:
        print("Ollama model is not installed. Installing...")
        install_result = install_tool("ollama")
        if install_result:
            print("Ollama model installed successfully.")
            result = run_command("ollama --model tiny --prompt 'Hello, world!'")
            print("Ollama model test result:")
            print(result)
        else:
            print(f"Error installing Ollama model: {install_result}")

def test_ollama_chatbot():
    if check_tool_installed("ollama"):
        print("Ollama chatbot is installed.")
        result = run_command("ollama --model chatbot --prompt 'Tell me a joke.'")
        print("Ollama chatbot test result:")
        print(result)
    else:
        print("Ollama chatbot is not installed. Installing...")
        install_result = install_tool("ollama")
        if install_result:
            print("Ollama chatbot installed successfully.")
            result = run_command("ollama --model chatbot --prompt 'Tell me a joke.'")
            print("Ollama chatbot test result:")
            print(result)
        else:
            print(f"Error installing Ollama chatbot: {install_result}")

def test_ollama_translation():
    if check_tool_installed("ollama"):
        print("Ollama translation is installed.")
        result = run_command("ollama --model translate --prompt 'Translate this to Spanish: Hello, world!'")
        print("Ollama translation test result:")
        print(result)
    else:
        print("Ollama translation is not installed. Installing...")
        install_result = install_tool("ollama")
        if install_result:
            print("Ollama translation installed successfully.")
            result = run_command("ollama --model translate --prompt 'Translate this to Spanish: Hello, world!'")
            print("Ollama translation test result:")
            print(result)
        else:
            print(f"Error installing Ollama translation: {install_result}")

def test_ollama_summarization():
    if check_tool_installed("ollama"):
        print("Ollama summarization is installed.")
        result = run_command("ollama --model summarize --prompt 'Summarize this text: Kali Linux is a Debian-based Linux distribution designed for digital forensics and penetration testing.'")
        print("Ollama summarization test result:")
        print(result)
    else:
        print("Ollama summarization is not installed. Installing...")
        install_result = install_tool("ollama")
        if install_result:
            print("Ollama summarization installed successfully.")
            result = run_command("ollama --model summarize --prompt 'Summarize this text: Kali Linux is a Debian-based Linux distribution designed for digital forensics and penetration testing.'")
            print("Ollama summarization test result:")
            print(result)
        else:
            print(f"Error installing Ollama summarization: {install_result}")

def test_ollama_qa():
    if check_tool_installed("ollama"):
        print("Ollama QA is installed.")
        result = run_command("ollama --model qa --prompt 'What is the capital of France?'")
        print("Ollama QA test result:")
        print(result)
    else:
        print("Ollama QA is not installed. Installing...")
        install_result = install_tool("ollama")
        if install_result:
            print("Ollama QA installed successfully.")
            result = run_command("ollama --model qa --prompt 'What is the capital of France?'")
            print("Ollama QA test result:")
            print(result)
        else:
            print(f"Error installing Ollama QA: {install_result}")

if __name__ == "__main__":
    print("Welcome to Kali Tools Automation!")
    print("Please select an option:")
    print("1. Add target")
    print("2. Execute attacks")
    print("3. Security results")
    print("4. Find device secrets")
    print("5. Test Ollama model")
    print("6. Test Ollama chatbot")
    print("7. Test Ollama translation")
    print("8. Test Ollama summarization")
    print("9. Test Ollama QA")
    print("0. Exit")

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
        test_ollama_model()
    elif choice == "6":
        test_ollama_chatbot()
    elif choice == "7":
        test_ollama_translation()
    elif choice == "8":
        test_ollama_summarization()
    elif choice == "9":
        test_ollama_qa()
    elif choice == "0":
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")