import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("Sticky Keyboard test")

tkinter.Button(text = "Q").pack(side= tkinter.TOP, anchor= tkinter.N)
tkinter.Button(text = "Q").pack(side= tkinter.TOP, anchor= tkinter.N)
tkinter.Button(text = "Q").pack(side= tkinter.TOP, anchor= tkinter.N)
tkinter.Button(text = "Q").pack(side= tkinter.TOP, anchor= tkinter.N)
tkinter.Button(text = "Q").pack(side= tkinter.TOP, anchor= tkinter.N)
tkinter.Button(text = "Q").pack(side= tkinter.TOP, anchor= tkinter.N)

E1 = tkinter.Entry(root)

E1.pack(side = tkinter.TOP, anchor = tkinter.N)

root.mainloop()
