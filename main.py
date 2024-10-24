import tkinter
import customtkinter as ctk 
from pytube import YouTube


# app vinduet
app = ctk.CTk()
app.geometry ("400x600")
app.title ("YouTube MP4 Downloader")
ctk.set_appearance_mode("system")

# Tekst i vinduet
title = ctk.CTkLabel(app, text="Legg til en YouTube lenke")
title.pack(padx=10, pady=10)

#tekst felte for lenken til videon  
url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=300, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Lar appen kjøre
app.mainloop()