import tkinter as tk

counter = 0

def add_label(event=None):

    global counter

    if counter > 7:
        counter = 0   
        children = frame.winfo_children()
        for i in children:
            if isinstance(i, tk.Label):
                i.destroy()

    new_text = entry.get().strip()

    if len(new_text) <= 2:
        error_label.configure(text='enter three symbols at least')
        return

    error_label.configure(text='')
    entry.delete(0, tk.END)
    new_label = tk.Label(frame, text=new_text, padx=50, pady=10)

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

frame = tk.Frame(window)
frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

entry = tk.Entry(window, width=20)
entry.pack(side=tk.TOP)
entry.bind('<Return>', add_label)
entry.focus_set()

error_label = tk.Label(window, text='', 
                       font=('Times New Roman', 12), fg='red')
error_label.pack()

window.mainloop()