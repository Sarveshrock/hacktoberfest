import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def load_dictionary():
    dictionary = {}
    try:
        with open("dictionary.txt", "r") as file:
            for line in file:
                word, meaning = line.strip().split(":")
                dictionary[word.strip()] = meaning.strip()
    except FileNotFoundError:
        with open("dictionary.txt", "w") as file:
            pass
    return dictionary

def save_dictionary(dictionary):
    with open("dictionary.txt", "w") as file:
        for word, meaning in sorted(dictionary.items()):
            file.write(f"{word}: {meaning}\n")

def add_word():
    word = entry_word.get().strip().capitalize()
    meaning = entry_meaning.get().strip()
    if word and meaning:
        dictionary[word] = meaning
        save_dictionary(dictionary)
        messagebox.showinfo("Success", "Word added to the dictionary.")
        entry_word.delete(0, tk.END)
        entry_meaning.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Both word and meaning are required.")

def find_meaning():
    word = entry_word.get().strip()
    meaning = dictionary.get(word, "Word not found in the dictionary.")
    messagebox.showinfo("Meaning", meaning)

def remove_word():
    word = entry_word.get().strip().capitalize()
    if word in dictionary:
        del dictionary[word]
        save_dictionary(dictionary)
        messagebox.showinfo("Success", f"{word} and its meaning removed from the dictionary.")
        entry_word.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Word not found in the dictionary.")

def on_exit():
    save_dictionary(dictionary)
    root.destroy()

dictionary = load_dictionary()

root = tk.Tk()
root.title("Dictionary GUI Tool")

root.geometry("315x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), foreground="black", borderwidth=0)

label_title = tk.Label(root, text="Dictionary Tool", bg="#FFFF00", font=("Helvetica", 18, "bold"))
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label_word = tk.Label(root, text="Word:", bg="#f0f0f0", font=("Helvetica", 12))
label_word.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_word = tk.Entry(root, font=("Helvetica", 12), width=20)
entry_word.grid(row=1, column=1, padx=5, pady=5)

label_meaning = tk.Label(root, text="Meaning:", bg="#f0f0f0", font=("Helvetica", 12))
label_meaning.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_meaning = tk.Entry(root, font=("Helvetica", 12), width=20)
entry_meaning.grid(row=2, column=1, padx=5, pady=5)

button_add = ttk.Button(root, text="Add Word", command=add_word, style="AddButton.TButton")
style.configure("AddButton.TButton", background="#4CAF50")
button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

button_find = ttk.Button(root, text="Find Meaning", command=find_meaning, style="FindButton.TButton")
style.configure("FindButton.TButton", background="#FFD700")
button_find.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

button_remove = ttk.Button(root, text="Remove Word", command=remove_word, style="RemoveButton.TButton")
style.configure("RemoveButton.TButton", background="#FF4500")
button_remove.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
