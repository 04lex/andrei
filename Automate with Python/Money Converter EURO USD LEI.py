import tkinter as tk

root = tk.Tk()

root.geometry("400x400")
root.title("Converter EURO - USD - LEI")

#Euro
Label1 = tk.Label(root, text="Euro", font=("Arial", 24))
Label1.pack()
Entry1 = tk.Entry(root)
Entry1.pack()
#USD
Label2 = tk.Label(root, text="USD", font=("Arial", 24))
Label2.pack()
Entry2 = tk.Entry(root)
Entry2.pack()
#Lei
Label3 = tk.Label(root, text="LEI", font=("Arial", 24))
Label3.pack()
Entry3 = tk.Entry(root)
Entry3.pack()


def Euro():
    euro = Entry1.get()
    usd = float(euro) * 1.18
    lei = float(euro) * 4.86
    Entry2.delete(0, tk.END)
    Entry2.insert(0, usd)
    Entry3.delete(0, tk.END)
    Entry3.insert(0, lei)
    
def Usd():
    usd = Entry2.get()
    euro = float(usd) * 0.85
    lei = float(usd) * 4.13
    Entry1.delete(0, tk.END)
    Entry1.insert(0, euro) 
    Entry3.delete(0, tk.END) 
    Entry3.insert(0, lei) 
    
def Lei():
    lei = Entry3.get()
    euro = float(lei) * 0.21
    usd = float(lei) * 0.24
    Entry1.delete(0, tk.END)
    Entry1.insert(0, euro)
    Entry2.delete(0, tk.END)
    Entry2.insert(0, usd)

button1 = tk.Button(root, text="Euro", font=("Arial", 14))
button1.pack(padx=20, pady=20)
button1.config(command=Euro)

button2 = tk.Button(root, text="USD", font=("Arial", 14))
button2.pack(padx=20, pady=20)
button2.config(command=Usd)

button3 = tk.Button(root, text="LEI", font=("Arial", 14))
button3.pack(padx=20, pady=20)
button3.config(command=Lei)


 




root.mainloop()