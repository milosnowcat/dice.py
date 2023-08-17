# TODO hacer un programa que elija un número random del 1 al 6
# y que lo muestre en una ventana usando una imagen de un dado
# con el número elegido

import tkinter as ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

root = ttk.Window(themename="vapor")
root.title("Dice.py")
root.geometry("700x400")

frm = ttk.Frame(root)
frm.pack(padx=30, pady=40)

number_image = "assets/images/cat.png"
dice_image = ImageTk.PhotoImage(Image.open(number_image).resize((200, 200)))
ttk.Label(frm, image=dice_image).pack()

ttk.Button(frm, text="Roll Dice").pack(pady=20)

root.mainloop()
