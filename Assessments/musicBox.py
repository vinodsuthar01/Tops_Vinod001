import tkinter as tk
import os
from tkinter import messagebox

class Playlist:
    def __init__(self, folder="Playlists"):
        self.folder = folder
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

    def create_playlist(self, name):
        if not name:
            messagebox.showwarning("Warning", "Enter playlist name")
            return

        filename = name + ".txt"
        path = os.path.join(self.folder, filename)

        if os.path.exists(path):
            messagebox.showerror("Error", "Playlist already exists")
            return

        with open(path, "w") as f:
            f.write("song1\nsong2\nsong3\nsong4")

        messagebox.showinfo("Success", "Playlist created")

    def get_playlists(self):
        return [f for f in os.listdir(self.folder) if f.endswith(".txt")]


# ---------------- GUI ----------------
root = tk.Tk()
root.geometry("400x450")
root.title("Playlist Manager")

p = Playlist()

# Entry
tk.Label(root, text="Playlist Name").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Text Widget
text = tk.Text(root, width=40, height=12)
text.pack(pady=10)

# Functions
def create():
    p.create_playlist(entry.get())
    entry.delete(0, tk.END)

def view():
    text.delete("1.0", tk.END)
    playlists = p.get_playlists()

    if not playlists:
        text.insert(tk.END, "No playlists found")
        return

    for pl in playlists:
        text.insert(tk.END, pl + "\n")

def exit_app():
    root.destroy()

# Buttons
tk.Button(root, text="CREATE PLAYLIST", width=20, command=create).pack(pady=5)
tk.Button(root, text="VIEW PLAYLISTS", width=20, command=view).pack(pady=5)
tk.Button(root, text="EXIT", width=20, command=exit_app).pack(pady=5)

root.mainloop()
