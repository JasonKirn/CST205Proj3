from tkinter import *
#from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Sticky keyboard test: Now with more grids")

        for r in range(4):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="{0}".format(c), height = 1).grid(row=0,column=c,sticky=E+W)

        Frame1 = Frame(master)
        Frame1.grid(row = 1, column = 0, rowspan = 1, columnspan = 5, sticky = W+E+N+S)
        Frame2 = Frame(master)
        Frame2.grid(row = 2, column = 0, rowspan = 1, columnspan = 5, sticky = W+E+N+S)
        Frame3 = Frame(master)
        Frame3.grid(row = 3, column = 0, rowspan = 1, columnspan = 5, sticky = W+E+N+S)

        #Row2
        QButton = Button(Frame1, text = "Q").grid(row = 0, column = 0, sticky = W+E+N+S)
        WButton = Button(Frame1, text = "W").grid(row = 0, column = 1, sticky = W+E+N+S, padx = 4)
        EButton = Button(Frame1, text = "E").grid(row = 0, column = 2, sticky = W+E+N+S, padx = 3)
        RButton = Button(Frame1, text = "R").grid(row = 0, column = 3, sticky = W+E+N+S, padx = 3)
        TButton = Button(Frame1, text = "T").grid(row = 0, column = 4, sticky = W+E+N+S, padx = 3)
        YButton = Button(Frame1, text = "Y").grid(row = 0, column = 5, sticky = W+E+N+S, padx = 3)
        UButton = Button(Frame1, text = "U").grid(row = 0, column = 6, sticky = W+E+N+S, padx = 3)
        IButton = Button(Frame1, text = "I").grid(row = 0, column = 7, sticky = W+E+N+S, padx = 3)
        OButton = Button(Frame1, text = "O").grid(row = 0, column = 8, sticky = W+E+N+S, padx = 3)
        PButton = Button(Frame1, text = "P").grid(row = 0, column = 9, sticky = W+E+N+S, padx = 3)
        #Row3
        AButton = Button(Frame2, text = "A").grid(row = 0, column = 0, sticky = W+E+N+S, padx = 5)
        SButton = Button(Frame2, text = "S").grid(row = 0, column = 1, sticky = W+E+N+S, padx = 5)
        DButton = Button(Frame2, text = "D").grid(row = 0, column = 2, sticky = W+E+N+S, padx = 5)
        FButton = Button(Frame2, text = "F").grid(row = 0, column = 3, sticky = W+E+N+S, padx = 5)
        GButton = Button(Frame2, text = "G").grid(row = 0, column = 4, sticky = W+E+N+S, padx = 5)
        HButton = Button(Frame2, text = "H").grid(row = 0, column = 5, sticky = W+E+N+S, padx = 5)
        JButton = Button(Frame2, text = "J").grid(row = 0, column = 6, sticky = W+E+N+S, padx = 5)
        KButton = Button(Frame2, text = "K").grid(row = 0, column = 7, sticky = W+E+N+S, padx = 5)
        LButton = Button(Frame2, text = "L").grid(row = 0, column = 8, sticky = W+E+N+S, padx = 5)
        #Row4
        #ZButton = Button(Frame3, text = "Z").grid(row = 0, column = 0, sticky = W+E+N+S, padx = 8)
        #XButton = Button(Frame3, text = "X").grid(row = 0, column = 1, sticky = W+E+N+S, padx = 6)
        #CButton = Button(Frame3, text = "C").grid(row = 0, column = 2, sticky = W+E+N+S, padx = 6)
        #VButton = Button(Frame3, text = "V").grid(row = 0, column = 3, sticky = W+E+N+S, padx = 6)
        #BButton = Button(Frame3, text = "B").grid(row = 0, column = 4, sticky = W+E+N+S, padx = 6)
        #NButton = Button(Frame3, text = "N").grid(row = 0, column = 5, sticky = W+E+N+S, padx = 6)
        #MButton = Button(Frame3, text = "M").grid(row = 0, column = 6, sticky = W+E+N+S, padx = 6)

        ZButton = Button(Frame3, text = " Z ", padx = 10).pack(side=LEFT, fill = BOTH)
        XButton = Button(Frame3, text = " X ").pack(side=LEFT)
        CButton = Button(Frame3, text = " C ").pack(side=LEFT)
        VButton = Button(Frame3, text = "V").pack(side=LEFT)
        BButton = Button(Frame3, text = "B").pack(side=LEFT)
        NButton = Button(Frame3, text = "N").pack(side=LEFT)
        MButton = Button(Frame3, text = "M").pack(side=LEFT)

root = Tk()
app = Application(master = root)
#app.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(275,400))
#app.focus_set()  # <-- move focus to this widget
#app.bind("<Escape>", lambda e: app.quit())
app.mainloop()

#tkinter.Button(text = "Set 1").grid(row = 0, column = 0)
#tkinter.Button(text = "Set 2").grid(row = 0, column = 1)
#tkinter.Button(text = "Set 3").grid(row = 0, column = 2)
#tkinter.Button(text = "Set 4").grid(row = 0, column = 3)
#tkinter.Button(text = "Set 5").grid(row = 0, column = 4)
#tkinter.Button(text = "Q").grid(row = 2, column = 0, sticky = "e")
#tkinter.Button(text = "W").grid(row = 2, column = 1)
#tkinter.Button(text = "E").grid(row = 2, column = 2), expand = yes)
#tkinter.Button(text = "R").grid(row = 2, column = 3)
#tkinter.Button(text = "T").grid(row = 2, column = 4)
#tkinter.Button(text = "Y").grid(row = 2, column = 5)
#tkinter.Button(text = "U").grid(row = 2, column = 6)
#tkinter.Button(text = "I").grid(row = 2, column = 7)
#tkinter.Button(text = "O").grid(row = 2, column = 8)
#tkinter.Button(text = "P").grid(row = 2, column = 9)


###E1 = tkinter.Entry(root)

#E1.grid(side = tkinter.TOP, anchor = tkinter.N)###

#root.mainloop()
