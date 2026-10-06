#!/usr/bin/env python3

import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess

def list_open_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    host = '127.0.0.1'
    start_port = 1
    end_port = 1024
    print(f"Scanning {host} for open ports in range {start_port}-{end_port}...")
    open_ports = list_open_ports(host, start_port, end_port)
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found.")

class ToolSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Selector")
        
        self.selected_tool = tk.StringVar()
        self.selected_target = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Select Tool:").grid(row=0, column=0, padx=10, pady=10)
        tk.Radiobutton(self.root, text="Scam Open Port", variable=self.selected_tool, value="scam_open_port").grid(row=0, column=1, padx=10, pady=10)
        tk.Radiobutton(self.root, text="File Selector", variable=self.selected_tool, value="file_selector").grid(row=0, column=2, padx=10, pady=10)
        tk.Radiobutton(self.root, text="John and Harcart", variable=self.selected_tool, value="john_and_harcart").grid(row=0, column=3, padx=10, pady=10)
        
        tk.Label(self.root, text="Select Target:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.selected_target, width=50).grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        
        tk.Button(self.root, text="Run Tool", command=self.run_tool).grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    
    def run_tool(self):
        tool = self.selected_tool.get()
        target = self.selected_target.get()
        
        if not tool or not target:
            messagebox.showerror("Error", "Please select a tool and provide a target.")
            return
        
        if tool == "scam_open_port":
            self.run_scam_open_port(target)
        elif tool == "file_selector":
            self.run_file_selector(target)
        elif tool == "john_and_harcart":
            self.run_john_and_harcart(target)
    
    def run_scam_open_port(self, target):
        try:
            result = subprocess.run(['python3', 'list_ports.py', target], capture_output=True, text=True, check=True)
            messagebox.showinfo("Result", result.stdout)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", e.stderr)
    
    def run_file_selector(self, target):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            messagebox.showinfo("Selected File", f"Selected file: {file_path}")
    
    def run_john_and_harcart(self, target):
        messagebox.showinfo("Running", "Running John and Harcart on target: " + target)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToolSelectorApp(root)
    root.mainloop()
