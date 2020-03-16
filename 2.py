import tkinter as tk
import tkinter.messagebox

def open_results():
    tkinter.messagebox.showinfo('Summary', 'test')

window = tk.Tk()

button = tk.Button(window, text='Submit', command=open_results)
button.pack(side=tk.BOTTOM, fill=tk.X)

radio_frame = tk.Frame(window)
radio_frame.pack(side=tk.BOTTOM)

cb_var_1 = tk.IntVar()
cb_var_2 = tk.IntVar()

tk.Checkbutton(window, text="I have a degree", variable=cb_var_1).pack()
tk.Checkbutton(window, text="I'm not a robot", variable=cb_var_2).pack()

state_of_radio = tk.StringVar()
state_of_radio.set('3')
tk.Radiobutton(radio_frame, text="5", variable=state_of_radio, value="5").pack(side=tk.RIGHT)
tk.Radiobutton(radio_frame, text="4", variable=state_of_radio, value="4").pack(side=tk.RIGHT)
tk.Radiobutton(radio_frame, text="3", variable=state_of_radio, value="3").pack(side=tk.RIGHT)

scaler = tk.Scale(window, from_=10, to=30, orient='horizontal', 
                resolution=5)
scaler.pack()


spin = tk.Spinbox(window, values=('Primary School', 'Secondary School', 'College'))
spin.pack(side=tk.BOTTOM, padx=10, pady=15, ipady=5)

window.mainloop()
