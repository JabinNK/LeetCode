from tkinter import*
import math

def evaluer(event):
 text.configure(text="result:"+str(eval(entree.get())))

 windows = Tk()
 window.title("calculator")
 window.confi(bg='grey')
 entree= Entry(window)
 entree.bind("<return>",evaluer)
 texte = Label(window,fg='black',bg='grey')
 entree.pack()
 texte.pack()
 window.mainloop()