import tkinter as tk

counter = 0

def add_label(event=None):

    global counter

    new_text = entry.get().strip()

    if len(new_text) <= 2:
        return

    entry.delete(0, tk.END)
    new_label = tk.Label(window, text=new_text, padx=50, pady=10)

    if counter % 2:
        new_label.configure(bg="grey", fg="white")
    else:
        new_label.configure(bg="white", fg="black")

    new_label.pack(side=tk.TOP, fill=tk.X)
    counter += 1


window = tk.Tk()
window.geometry("300x500")

tk.Label(window, text="Test Program", padx=50, pady=20, font=('Times New Roman', 30)).pack(side=tk.BOTTOM)
tk.Button(window, text='Click Me!', padx=10, pady=5, command=add_label).pack(fill=tk.X)

entry = tk.Entry(window, width=20)
entry.pack(side=tk.TOP)
entry.bind('<Return>', add_label)
entry.focus_set()

window.mainloop()