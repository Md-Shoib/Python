import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import sys
import io
import json

class CodeCell:
    def __init__(self, master, code="", output="", namespace=None):
        self.master = master
        self.namespace = namespace if namespace is not None else {}

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.input_area = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=10, width=80)
        self.input_area.insert(tk.END, code)
        self.input_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.output_area = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=10, width=80)
        self.output_area.insert(tk.END, output)
        self.output_area.config(state=tk.DISABLED)
        self.output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.execute_button = tk.Button(self.frame, text="Execute", command=self.execute_code)
        self.execute_button.pack(pady=5)

    def execute_code(self):
        code = self.input_area.get("1.0", tk.END)
        output = io.StringIO()
        sys.stdout = output

        try:
            exec(code, self.namespace)
        except Exception as e:
            output.write(f"Error: {str(e)}")

        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, output.getvalue())
        self.output_area.config(state=tk.DISABLED)

        sys.stdout = sys.__stdout__

    def get_code(self):
        return self.input_area.get("1.0", tk.END).strip()

    def get_output(self):
        return self.output_area.get("1.0", tk.END).strip()

class JupyterNotebookClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Jupyter Notebook Clone")
        self.cells = []
        self.shared_namespace = {}

        self.notebook_frame = tk.Frame(root)
        self.notebook_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.add_cell_button = tk.Button(root, text="Add Code Cell", command=self.add_code_cell)
        self.add_cell_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Notebook", command=self.save_notebook)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Load Notebook", command=self.load_notebook)
        self.load_button.pack(pady=5)

        self.add_code_cell()

    def add_code_cell(self, code="", output=""):
        cell = CodeCell(self.notebook_frame, code, output, self.shared_namespace)
        self.cells.append(cell)

    def save_notebook(self):
        notebook_data = []
        for cell in self.cells:
            notebook_data.append({
                "code": cell.get_code(),
                "output": cell.get_output()
            })
        filepath = filedialog.asksaveasfilename(defaultextension=".ipynb", filetypes=[("Jupyter Notebook", "*.ipynb")])
        if filepath:
            with open(filepath, 'w') as f:
                json.dump(notebook_data, f)
            messagebox.showinfo("Success", "Notebook saved successfully.")

    def load_notebook(self):
        filepath = filedialog.askopenfilename(filetypes=[("Jupyter Notebook", "*.ipynb")])
        if filepath:
            try:
                with open(filepath, 'r') as f:
                    notebook_data = json.load(f)

                for cell in self.cells:
                    cell.frame.destroy()
                self.cells = []

                for cell_data in notebook_data:
                    self.add_code_cell(cell_data["code"], cell_data["output"])

                messagebox.showinfo("Success", "Notebook loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load notebook: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    notebook = JupyterNotebookClone(root)
    root.mainloop()