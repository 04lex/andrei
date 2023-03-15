import tkinter as tk
from pytube import YouTube

root=tk.Tk()
root.title("Youtube Downloader")
root.geometry("500x500")
Label= tk.Label(root, text="Adauga link ul de la video ul pe care vrei sa il descarci", font=("Arial", 24))
Label.pack(padx=20, pady=20)

textbox = tk.Entry(root, width=50)
textbox.pack()

button = tk.Button(root, text="Download", font=("Arial", 14))
button.pack(padx=20, pady=20)

def download():
    link = textbox.get()
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download()
    Labelresult = tk.Label(root, text="Downloaded", font=("Arial", 24))
    Labelresult.pack(padx=20, pady=20)
    
button.config(command=download)

root.mainloop()