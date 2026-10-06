import os
import powershell
import subprocess
import sys

def run_command(command, use_powershell=False):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, use_powershell=False)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

def test_network(use_powershell=False):
    print("Starting network test...")
    result = run_command("ping -c 4 127.0.0.1")
    print("Network test result:")
    print(result)

def test_disk_space():
    print("Starting disk space test...")
    result = run_command("df -h")
    print("Disk space test result:")
    print(result)

def test_python_version():
    print("Starting Python version test...")
    result = run_command("python3 --version")
    print("Python version test result:")
    print(result)

def test_top_10_kali_tools():
    print("Starting top 10 Kali Linux tools test...")
    result = run_command("ls /usr/share/kali-linux-tools | head -n 10")
    print("Top 10 Kali Linux tools test result:")
    print(result)

def create_html_button():
    html_button = """
    <html>
    <head>
        <title>Auto Button</title>
    </head>
    <body>
        <button onclick="alert('Button clicked!')">Click Me</button>
    </body>
    </html>
    """
    with open("auto_button.html", "w") as file:
        file.write(html_button)
    print("HTML button created.")

def start_conversation():
    print("Starting conversation with IA...")
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("IA: Goodbye!")
        sys.exit(0)
    else:
        response = run_command(f"echo '{user_input}' | python3 /path/to/ia_model.py")
        print(f"IA: {response}")

if __name__ == "__main__":
    print("Starting Kali Linux test suite...")
    test_network()
    test_disk_space()
    test_python_version()
    test_top_10_kali_tools()
    create_html_button()
    print("Kali Linux test suite completed.")
    print("Starting conversation with IA...")
    start_conversation()