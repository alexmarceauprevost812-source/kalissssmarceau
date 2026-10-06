import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess

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
        tk.Radiobutton(self.root, text="Analyze Web SQL Injection", variable=self.selected_tool, value="analyze_web_sql_injection").grid(row=0, column=4, padx=10, pady=10)
        
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
        elif tool == "analyze_web_sql_injection":
            self.run_analyze_web_sql_injection(target)
    
    def run_scam_open_port(self, target):
        try:
            python_cmd = "python" if subprocess.os.name == "nt" else "python3"
            result = subprocess.run(
                [python_cmd, "list_ports.py", target],
                capture_output=True,
                text=True,
                check=True,
            )
            messagebox.showinfo("Résultat", result.stdout)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erreur", (e.stderr or e.stdout or "Le scan a échoué.").strip())
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
    
    def run_file_selector(self, target):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            messagebox.showinfo("Selected File", f"Selected file: {file_path}")
    
    def run_john_and_harcart(self, target):
        messagebox.showinfo("Running", "Running John and Harcart on target: " + target)
    
    def run_analyze_web_sql_injection(self, target):
        messagebox.showinfo("Running", "Analyzing Web SQL Injection on target: " + target)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToolSelectorApp(root)
    root.mainloop()
