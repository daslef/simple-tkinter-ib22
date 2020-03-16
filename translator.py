import requests
import tkinter as tk
import tkinter.ttk

YA_TOKEN = 'trnsl.1.1.20200228T124248Z.23d3f30fe1bc309f.8c9ccda6143f22ccb6fb89bef10fbdec79b24dca'
REQUEST = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'


def translate_en_ru():
    text = en_text.get(1.0, tk.END)
    r = requests.get(REQUEST.format(YA_TOKEN, text, 'en-ru'))
    print(r.json()['text'][0])


window = tk.Tk()
window.geometry('500x300')
window.resizable(False, False)

tk.Button(window, text='Translate!', command=translate_en_ru).pack(side=tk.BOTTOM)

notebook = tkinter.ttk.Notebook(window)
notebook.pack(fill=tk.BOTH)

en_frame = tk.Frame(window)
ru_frame = tk.Frame(window)
en_text = tk.Text(en_frame)
ru_text = tk.Text(ru_frame)

en_frame.pack()
ru_frame.pack()
en_text.pack()
ru_text.pack()

notebook.add(en_frame, text='English')
notebook.add(ru_frame, text='Russian')

window.mainloop()