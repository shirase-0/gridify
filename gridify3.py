#print("Hello Sara!")
#print("Hello Tim!")

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#reference = Image.open()

window = tk.Tk()
frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1, row=0)

window.mainloop()
