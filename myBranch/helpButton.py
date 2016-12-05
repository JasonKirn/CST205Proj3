from tkinter import *

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.master.title("Instructions")

        ###theFrame = Frame(master, background = "blue")

        Label1 = Label(self, wraplength = 275, justify = LEFT, text="Instructions:  To use this program, press any keyboard key to play a sound.\n  The numbers '1-9' play repeating noises.  You can use these for a consistent beat.\n  If you want to pick your own noises, use edit mode to map different noises to different keys.\n  We included some editable sound files for you to use in edit mode.").pack(side = LEFT, anchor = N)

        BackButton = Button(text = "Back").pack(anchor = S)
root = Tk()
app = Application(master = root)

root.geometry("{0}x{1}+0+0".format(275,400))

app.mainloop()
