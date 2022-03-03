#print("Hello Sara!")
#print("Hello Tim!")

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

window = Tk()
window.title("Gridify")


def openfile():
	global reference
	# TODO: limit this dialog box to only png, jpg, and jpeg files
	window.filename = filedialog.askopenfilename(title="Select an image")
	reference = ImageTk.PhotoImage(Image.open(window.filename))
	reference_label = Label(window, image=reference).pack()

quitbutton = Button(window, text="Quit", command=window.destroy).pack()
openbutton = Button(window, text="Open Image", command=openfile).pack()

window.mainloop()
