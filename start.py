import tkinter as tk
from generator import *

root = tk.Tk()

def generateNew():
    createNewRhythm()

root.title("Eh Fuck Off M8")
root.geometry('500x250')

titleLabel = tk.Label(root, text="Wreckage Generator")
titleLabel.pack()

generateButton = tk.Button(root, text='Generate New', width=50, command=generateNew)
generateButton.pack()

root.mainloop()