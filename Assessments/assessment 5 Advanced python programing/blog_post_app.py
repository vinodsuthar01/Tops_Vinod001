import os
from tkinter import *
from tkinter import messagebox

# Post Class
class Post:
    def __init__(self, username, title, content):
        self.username = username
        self.title = title
        self.content = content

    def save_to_file(self):
        filename = f"{self.username}_{self.title}.txt".replace(" ", "_")
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Author: {self.username}\n")
                file.write(f"Title: {self.title}\n\n")
                file.write(self.content)
            return filename
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save post:\n{e}")
            return None


# Main App Class
class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog App")
        self.root.geometry("520x600")

        self.current_file = None

        Label(root, text="Username").pack()
        self.username_entry = Entry(root, width=50)
        self.username_entry.pack()

        Label(root, text="Post Title").pack()
        self.title_entry = Entry(root, width=50)
        self.title_entry.pack()

        Label(root, text="Content").pack()
        self.content_text = Text(root, height=8, width=50)
        self.content_text.pack()

        Button(root, text="Save Post", command=self.save_post).pack(pady=5)

        Label(root, text="Saved Posts").pack()

        self.post_listbox = Listbox(root, width=60)
        self.post_listbox.pack()

        Button(root, text="View Post", command=self.view_post).pack(pady=3)
        Button(root, text="Edit Post", command=self.edit_post).pack(pady=3)
        Button(root, text="Delete Post", command=self.delete_post).pack(pady=3)

        Label(root, text="Post Display").pack()

        self.display_area = Text(root, height=10, width=60)
        self.display_area.pack()

        self.load_posts()

    def save_post(self):
        username = self.username_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", END).strip()

        if not username or not title or not content:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            if self.current_file:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(f"Author: {username}\n")
                    file.write(f"Title: {title}\n\n")
                    file.write(content)

                messagebox.showinfo("Updated", "Post updated successfully!")
                self.current_file = None

            else:
                post = Post(username, title, content)
                post.save_to_file()
                messagebox.showinfo("Success", "Post saved successfully!")

            self.load_posts()
            self.clear_fields()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_posts(self):
        self.post_listbox.delete(0, END)
        files = [f for f in os.listdir() if f.endswith(".txt")]

        for file in files:
            self.post_listbox.insert(END, file)

    def view_post(self):
        try:
            selected = self.post_listbox.get(self.post_listbox.curselection())

            with open(selected, "r", encoding="utf-8") as file:
                content = file.read()

            self.display_area.delete("1.0", END)
            self.display_area.insert(END, content)

        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a post")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")

    def edit_post(self):
        try:
            selected = self.post_listbox.get(self.post_listbox.curselection())

            with open(selected, "r", encoding="utf-8") as file:
                lines = file.readlines()

            username = lines[0].replace("Author: ", "").strip()
            title = lines[1].replace("Title: ", "").strip()
            content = "".join(lines[3:])

            self.username_entry.delete(0, END)
            self.username_entry.insert(0, username)

            self.title_entry.delete(0, END)
            self.title_entry.insert(0, title)

            self.content_text.delete("1.0", END)
            self.content_text.insert(END, content)

            self.current_file = selected

        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a post")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")

    def delete_post(self):
        try:
            selected = self.post_listbox.get(self.post_listbox.curselection())

            confirm = messagebox.askyesno("Confirm Delete", f"Delete {selected}?")
            if confirm:
                os.remove(selected)
                messagebox.showinfo("Deleted", "Post deleted successfully!")

                self.load_posts()
                self.display_area.delete("1.0", END)

        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a post")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")

    def clear_fields(self):
        self.username_entry.delete(0, END)
        self.title_entry.delete(0, END)
        self.content_text.delete("1.0", END)



# Run App

if __name__ == "__main__":
    root = Tk()
    app = MiniBlogApp(root)
    root.mainloop()