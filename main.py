import tkinter
import customtkinter as ctk
from yt_dlp import YoutubeDL

def startDownload():
    try:
        ytLink = link.get()
        ydl_opts = {
            'format': 'best', # velger beste kvalitet for videon
            'outtmpl': '%(title)s.%(ext)s', #setter fil navnet og fil type.
            'noplaylist': False, # Lar laste ned hele spillelisten
        }
        with YoutubeDL(ydl_opts) as ydl: # starter nedlastningen med tidligere valg
            ydl.download([ytLink]) # laster ned
    except Exception as e: # gir feilmelding hvis noe går galt
        print(f"YouTube link fungerer ikke: {e}")
    print("Video lastet ned")

# app vinduet
app = ctk.CTk()
app.geometry("400x600")
app.title("YouTube MP4 Downloader")
ctk.set_appearance_mode("system")

# Tekst i vinduet
title = ctk.CTkLabel(app, text="Legg til en YouTube lenke")
title.pack(padx=10, pady=10)

# tekstfelt for lenken til videoen  
url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=300, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Last ned-knappen
download = ctk.CTkButton(app, text="Last ned", command=startDownload)
download.pack(padx=10, pady=10)

# Lar appen kjøre
app.mainloop()
