# TODO hacer un programa que elija un número random del 1 al 6
# y que lo muestre en una ventana usando una imagen de un dado
# con el número elegido

import tkinter as ttk
import ttkbootstrap as ttk

root = ttk.Window(themename="vapor")
root.title("Dice.py")
root.geometry("700x400")

frm = ttk.Frame(root)
frm.pack(padx=30, pady=40)

dice_image = ttk.PhotoImage(file='assets/images/cat.png')
Label(frm, image=dice_image).pack()

ttk.Button(frm, text="Roll Dice").pack(pady=20)

root.mainloop()
