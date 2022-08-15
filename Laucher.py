import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk

from Format import musica, video


def Widgets():

    tittle = Label(root, text="Youtube Download", bg="#BEB1ED",
                   justify="center", font=("Ubuntu",  13, "bold"), fg="#FFFFFF")
    tittle.grid(row=0, column=2, pady=2, padx=0)
    link_label = Label(root, text="Link:", bg="#BEB1ED",
                       justify="left",  fg="#FFFFFF", font=("Ubuntu"))
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=link, justify="left")
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    options_label = Label(root, text="Opção:", bg="#BEB1ED",  fg="#FFFFFF")
    options_label.grid(row=1, column=3, pady=5, padx=5)

    vlist = ["Video", "Musica"]
    Combo = ttk.Combobox(root, values=vlist, textvariable=options,
                         justify="center", state="readonly")
    Combo.set("Video")
    Combo.grid(row=1, column=3, pady=5, padx=5)

    Download_Button = Button(root, text="Download", command=Download, width=15,
                             bg="#696283",  fg="#FFFFFF", font=("Ubuntu"), cursor="exchange")
    Download_Button.grid(row=2, column=2, pady=2, padx=2)


def Download():
    link_youtube = link.get()
    options_format = options.get()
    if options_format == 'Video':
        video(link_youtube)
    elif options_format == 'Musica':
        musica(link_youtube)

    print(options_format)
    # coloca if com a opcao de video ou musica + depois msg personalizada e tambem validador de link do youtube fazer o search
    messagebox.showinfo("Sucesso!",
                        "Seu Dowloand está salvo\n")


root = tk.Tk()
root.geometry("550x100")
root.resizable(False, False)
root.title("Video_Dowloander")
root.config(background="#BEB1ED")

# Pega o link
link = StringVar()
options = StringVar()

Widgets()

root.mainloop()
