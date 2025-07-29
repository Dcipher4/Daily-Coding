import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime


class FolderZipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Zipper for Upload")

        # Variables
        self.folder_path = tk.StringVar()
        self.zip_path = tk.StringVar()
        self.include_hidden = tk.BooleanVar(value=False)

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Folder selection
        tk.Label(self.root, text="Folder to Zip:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.folder_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse...", command=self.browse_folder).grid(row=0, column=2, padx=5, pady=5)

        # Output zip file
        tk.Label(self.root, text="Output Zip File:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.zip_path, width=50).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse...", command=self.browse_zip).grid(row=1, column=2, padx=5, pady=5)

        # Options
        tk.Checkbutton(self.root, text="Include hidden files", variable=self.include_hidden).grid(row=2, column=1,
                                                                                                  padx=5, pady=5,
                                                                                                  sticky="w")

        # Zip button
        tk.Button(self.root, text="Create Zip Archive", command=self.create_zip, bg="#4CAF50", fg="white").grid(row=3,
                                                                                                                column=1,
                                                                                                                pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
            # Set default zip file name
            folder_name = os.path.basename(folder_selected)
            default_zip = os.path.join(os.path.dirname(folder_selected),
                                       f"{folder_name}_{datetime.now().strftime('%Y%m%d')}.zip")
            self.zip_path.set(default_zip)

    def browse_zip(self):
        zip_selected = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
        )
        if zip_selected:
            self.zip_path.set(zip_selected)

    def create_zip(self):
        folder_path = self.folder_path.get()
        zip_path = self.zip_path.get()

        if not folder_path or not zip_path:
            messagebox.showerror("Error", "Please select both a folder and an output zip file")
            return

        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    # Skip hidden files and folders if not included
                    if not self.include_hidden.get():
                        files = [f for f in files if not f.startswith('.')]
                        dirs[:] = [d for d in dirs if not d.startswith('.')]

                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=folder_path)
                        zipf.write(file_path, arcname)

            messagebox.showinfo("Success", f"Folder successfully zipped to:\n{zip_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create zip file:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FolderZipperApp(root)
    root.mainloop()