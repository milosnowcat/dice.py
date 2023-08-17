# TODO hacer un programa que elija un número random del 1 al 6
# y que lo muestre en una ventana usando una imagen de un dado
# con el número elegido

import tkinter as ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import random

def update_image():
    number = random.randint(1, 6)
    dice_image = ImageTk.PhotoImage(Image.open(f"assets/images/diceMagenta{number}.png").resize((240, 240)))
    image_panel.config(image=dice_image)
    image_panel.image = dice_image

root = ttk.Window(themename="vapor")
root.title("Dice.py")
root.geometry("700x400")

frm = ttk.Frame(root)
frm.pack(padx=30, pady=40)

dice_image = ImageTk.PhotoImage(Image.open("assets/images/cat.png").resize((240, 240)))
image_panel = ttk.Label(frm, image=dice_image)
image_panel.pack()

ttk.Button(frm, text="Roll Dice", command=update_image).pack(pady=20)

root.mainloop()
