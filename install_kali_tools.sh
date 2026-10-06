```bash
#!/bin/bash
# install_kali_tools.sh

# Function to install a tool using apt-get
install_tool() {
    local tool=$1
    echo "Installing $tool..."
    sudo apt-get install -y $tool
    if [ $? -eq 0 ]; then
        echo "$tool installed successfully."
    else
        echo "Error installing $tool."
        exit 1
    fi
}

# Function to check if a tool is installed
check_tool_installed() {
    local tool=$1
    if command -v $tool &> /dev/null; then
        echo "$tool is installed."
        return 0
    else
        echo "$tool is not installed."
        return 1
    fi
}

# Main script
echo "Starting Kali Linux tools installation..."

# List of tools to install
tools=(
    "nmap"
    "metasploit-framework"
    "wireshark"
    "john"
    "hydra"
    "sqlmap"
    "burpsuite"
    "hashcat"
    "medusa"
    "nikto"
)

# Loop through the list and install each tool
for tool in "${tools[@]}"; do
    check_tool_installed $tool
    if [ $? -ne 0 ]; then
        install_tool $tool
    fi
done

echo "All Kali Linux tools installation completed."
```

This script will install a list of essential tools for Kali Linux. It checks if each tool is already installed and installs it if it is not. The script uses `apt-get` for package management and provides clear messages for each step of the installation process.