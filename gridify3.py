#print("Hello Sara!")
#print("Hello Tim!")

import sys
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

window = Tk()
window.title("Gridify")


def openfile():
	global reference
	# TODO: limit this dialog box to only png, jpg, and jpeg files
	window.filename = filedialog.askopenfilename(title="Select an image")
	reference = ImageTk.PhotoImage(Image.open(window.filename))
	reference_label = Label(window, image=reference).pack()

	with Image.open(window.filename) as im:
		draw = ImageDraw.Draw(im)
		#draw.line((0, 0) + im.size, fill=128)
		#draw.line((0, im.size[1], im.size[0], 0), fill=128)

		draw.line((5, 5) + im.size, fill=128)
		draw.line((500, 0, 500, 500), fill=128)

	#write to stdout
	im.save("test", "PNG")

quitbutton = Button(window, text="Quit", command=window.destroy).pack()
openbutton = Button(window, text="Open Image", command=openfile).pack()

# get image size in width and height as a tuple
#Image.size()



window.mainloop()

