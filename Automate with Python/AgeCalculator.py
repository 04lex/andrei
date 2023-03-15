import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

Label = tk.Label(root, text="Adauga-ti varsta", font=("Arial", 28))
Label.pack()

Entry1 = tk.Entry(root)
Entry1.pack()



def Calcul():    # invatat functii si clase python
    varsta = Entry1.get()
    varsta = int(varsta)
    varsta = 2023-varsta
    Label1 = tk.Label (root, text="Esti nascut in anul: " + str(varsta), font=("Arial", 28))
    Label1.pack()


    
button = tk.Button(root, text="Aflati varsta!",  font=("Arial", 12))
button.pack()
button.config(command=Calcul)




root.mainloop()