import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll Game")

dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200,200)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200,200)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2



label1.place(x = 20, y = 80)
label2.place(x = 280, y = 80)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200,200)))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200,200)))
    label2.configure(image = image2)
    label2.image = image2



button = tk.Button(window, text="ROLL", bg="Black", fg="White", font="times 20 bold", command=dice_roll)
button.place(x = 200, y = 10)


window.mainloop()