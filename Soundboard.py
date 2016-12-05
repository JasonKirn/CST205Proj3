from tkinter import *
from tkinter.filedialog import askopenfilename

from pygame import mixer
import os

#Create and initialize 36 paths for sounds
paths = [None for x in range(36)]
#Create and initialize 36 sounds
sounds = [None for x in range(36)]
#Create and initialize 36 buttons for sounds
buttons = [None for x in range(36)]
#Create and initialize 10 repeating sounds
repeating = [False for x in range(10)]
#Default sound_paths_file
sound_paths_file = "SoundPaths0.sndp"
#Label promp text
prompt = 'Play Mode\n Press a physical or virtual key to play a sound'
#Edit mode allows you to select sounds for keys
edit_mode = FALSE
#Help mode
help_shown = FALSE
#Initialize the mixer
mixer.init(44100)

#When 'Toggle Edit Mode' is select, we toggle the edit_mode boolean
def toggle_edit_mode():
    global edit_mode
    if edit_mode is TRUE:
        edit_mode = FALSE
        label.configure(text="Play Mode\n Press a physical or virtual key to play a sound", bg="light green")
    else:
        edit_mode = TRUE
        label.configure(text="Edit Mode\n Press a physical or virtual key to select a sound file", bg="yellow")

def show_help_menu():
    global help_shown
    if help_shown is TRUE:
        help_shown = FALSE
    else:
        help_shown = TRUE

def key_pressed(button, key=None):
    #If the button is not None, get its id
    if button is not None:
        key = button.id_string()

    # If the application is not in edit mode...
    if not edit_mode:
        # If the key is a numeric key...
        if key.isnumeric():
            # If there is a sound bound to the key...
            if sounds[int(key)] is not None:
                # If the sound isn't already repeating
                if repeating[int(key)] is False:
                    # Play on repeat
                    sounds[int(key)].play(-1)
                    # Set repeating for this sound to true
                    repeating[int(key)] = True
                    #While we're repeating, change our BG to yellow
                    buttons[int(key)].configure(bg="yellow")

                # If the sound is already repeating
                else:
                    # Set repeating to false for this sound
                    repeating[int(key)] = False
                    # Stop the sound
                    sounds[int(key)].stop()
                    # While we're not repeating, change our BG to light grey
                    buttons[int(key)].configure(bg="light grey")
        # If the key is a letter key...
        elif key.isalpha():
            # The key's letter converted to it's integer value - 87 = 10 - 35 (a - z)
            # If the sound at that position is not None...
            if sounds[ord(key) - 87] is not None:
                # Stop playing the sound if it's playing
                sounds[ord(key) - 87].stop()
                # And then start it again
                sounds[ord(key) - 87].play()
    # If we're in edit mode...
    else:
        # If this is a numeric key...
        if key.isnumeric():
            # Prompt the user to select a sound file
            file = askopenfilename(filetypes=[("Sound files","*.wav")])
            # Try to load that sound file in to the appropriate slot in the sounds dictionary
            try:
                sounds[int(key)] = mixer.Sound(file)
            # If it cannot be loaded, tell the user
            except:
                print("Unable to load sound " + file)

            # If the sound loaded correctly, set the path for that sound equal to the selected file
            if sounds[int(key)] is not None:
                paths[int(key)] = file
        # If this is an alpha key, we subtract 87 from it
        elif key.isalpha():
            # Prompt the user to select a sound file
            file = askopenfilename(filetypes=[("Sound files","*.wav")])

            # Try to load that sound file in to the appropriate slot in the sounds dictionary
            try:
                sounds[ord(key) - 87] = mixer.Sound(file)
            # If it cannot be loaded, tell the user
            except:
                print("Unable to load sounds " + file)

            # If the sound loaded correctly, set the path for that sound equal to the selected file
            if sounds[ord(key) - 87] is not None:
                paths[ord(key) - 87] = file


#Called by label1 when the user presses a key
def on_key(event):
        #If the event is a key symbol...
        if event.char == event.keysym:
            #Call the key pressed method and pass it the char pressed
            key_pressed(None,event.char)

#Count up until we find a number that doesn't have a corresponding file
#Then create one and write the sound keys and sound paths out as "key1:path1,key2:path2,..."
def save_sound_paths():
    i = 0
    #We create the .sndp extension here so that the file selection menu for the Sound Paths file only shows these files
    #sndp stands for S(ou)NDP(aths)
    while os.path.exists("SoundPaths" + str(i) + ".sndp") is True:
        i += 1

    print("New Sound Paths Saved as SoundPaths" + str(i) + ".txt")

    with open("SoundPaths" + str(i) + ".sndp", 'a') as file:
        k=0
        for p in paths:
            if p is not None:
                print("Saving " + p)

                #Add a comma if this isn't the first path
                if(k>0):
                    p = ","+p
                #Write the path
                file.write(p)
                k+=1
            else:
                p = "None"
                # Add a comma if this isn't the first path
                if (k > 0):
                    p = "," + p
                # Write the path
                file.write(p)
                k += 1
        file.close()


def load_sounds():
    global paths

    #For each path in the list of paths...
    i = 0
    for path in paths:
        if path is not None:
            try:
                if path != "None":
                    sounds[i] = mixer.Sound(path)
                    key = str(i)

                    if i >= 10:
                        key = str(chr(i+87))
                    print(path + " added to sounds on key '"+str(key)+"'")
            except:
                print("Invalid path "+path+", adding blank.")
            i+=1

def load_sound_paths(sound_paths_file=None):
    global paths

    if sound_paths_file is None:
        #We only show the .sndp files so that we can be sure they're in the right format (unless they've been tampered with)
        sound_paths_file = askopenfilename(filetypes=[("Sound Paths files","*.sndp")])
        print("Loading sound paths from file" + sound_paths_file)
    else:
        print("Loading sound paths from file" + sound_paths_file)

    try:
        #Open the paths file
        with open(sound_paths_file, 'r') as file:
            #Read the file's text as a string and split on commas
            read_paths = file.read().split(",")

            i = 0
            #For each path read, append it to our paths list
            for path in read_paths:
                if path is not None:
                    paths[i] = path
                else:
                    paths[i] = "None"
                i += 1
            file.close()
        load_sounds()
    except:
        print("Error loading Sound Paths file")

#Creates the virtual keyboard
def populate_frame_buttons(frame, lastButtonCount=1, asciiArray=None):
    #Set the total number of buttons equal to the total after the last row (default 1, because 0 comes at the end of the numeric row)
    totalButtonCount = lastButtonCount;

    #If asciiArray is not None, then we are creating an alphabetic row, so start at 0 and count up to the number of keys
    if asciiArray is not None:
        start = 0
        buttonCount = len(asciiArray)
    #Otherwise we're making a numeric row, so start at 1 and count to 10
    else:
        start = 1
        buttonCount = 10

    #Starting at start and ending at buttonCounter,
    for i in range(start,buttonCount):
        #Set the button's text to the ascii code for this char by adding the value in the asciiArray (1-26) to 96 (the ascii value for 'a')
        if asciiArray is not None:
            txt = str(chr(asciiArray[i]+96))
        #Otherwise, just set the text to 1-9 for the numeric row (We create 0 below)
        else:
            txt = str(i)

        #We create a subclass of Button so that we can make use of methods on that class for the button command
        #Also, the padx on this button is what determines its width, since it's pack() is set to fill and expand any extra space (IE the padding)
        buttons[totalButtonCount] = KeyButton(frame,text=txt,id=txt, command=key_pressed, padx=10)
        #Light grey is the default color for the buttons
        buttons[totalButtonCount].configure(bg="light grey")
        buttons[totalButtonCount].pack(side = LEFT, fill=BOTH, expand=1)
        #Increment the total number of buttons created
        totalButtonCount +=1

    #If asciiArray is None, we're making a numeric row and we've created 1 - 9, so not create 0
    if asciiArray is None:
        buttons[0] = KeyButton(frame, text="0", id="0", command=key_pressed, padx=10)
        buttons[0].configure(bg="light grey")
        buttons[0].pack(side=LEFT, fill=BOTH, expand=1)

    #Return the total number of buttons created after this row
    return totalButtonCount

#This class inherits from Button. It takes a command, but when the constructor for this class is called
#it uses it's own method (on_tk_command) as the base Button class command. The on_tk_command method
#calls the command that was passed to the KeyButton constructor, passing self as an argument. Using this
#self reference, we can get the id_string of the KeyButton that was pressed in the key_pressed method
class KeyButton(Button):
    def __init__(self, owner_widget, id=None, command=None, **args):
        Button.__init__( self, owner_widget, args, command=self.__on_tk_command)
        self.__id = id
        self.__specified_command = command

    def __on_tk_command(self):
        if self.__specified_command != None:
            self.__specified_command(self)
        else:
            self.on_clicked()

    def on_clicked(self):
        pass

    def id(self):
        return self.__id

    def id_string(self):
        return str(self.id());

if __name__ == "__main__":

    #Create the root window
    root = Tk()
    #Add a menu to the Tk window
    menu = Menu(root)
    # This sets the root's menu to the menu we created
    root.config(menu=menu)

    #Add a file submenu for
    fileMenu = Menu(menu, tearoff=0)
    fileMenu.add_command(label="Load Sound File", command=load_sound_paths)
    fileMenu.add_command(label="Save Sound File", command=save_sound_paths)
    fileMenu.add_separator()
    fileMenu.add_command(label="Quit", command=root.quit)
    #This is the command that puts all of the above in to a submenu of menu
    menu.add_cascade(label="File", menu=fileMenu)

    # Add an edit submenu for
    editMenu = Menu(menu, tearoff=0)
    editMenu.add_command(label="Toggle Edit Mode", command=toggle_edit_mode)
    # This is the command that puts all of the above in to a submenu of menu
    menu.add_cascade(label="Edit", menu=editMenu)

    # Add an help submenu for
    helpMenu = Menu(menu, tearoff=0)
    helpMenu.add_command(label="Help", command=show_help_page)
    # This is the command that puts all of the above in to a submenu of menu
    menu.add_cascade(label="Help", menu=helpMenu)

    #Create a frame to store each of the rows of buttons
    content = Frame(root)
    content.pack()

    #Create the top numeric row
    finalButtonCount = 0
    numericRow = Frame(content)
    numericRow.pack()
    finalButtonCount = populate_frame_buttons(numericRow)

    #Create the 1st alphabetic row
    alpha1Row = Frame(content)
    alpha1Row.pack()
    a1Row = [17,23,5,18,20,25,21,9,15,16]
    finalButtonCount = populate_frame_buttons(alpha1Row, finalButtonCount, a1Row)

    #Create the 2nd alphabetic row
    alpha2Row = Frame(content)
    alpha2Row.pack()
    a2Row = [1, 19, 4, 6, 7, 8, 10, 11, 12]
    finalButtonCount = populate_frame_buttons(alpha2Row, finalButtonCount, a2Row)

    #Create the 3rd alphabetic row
    alpha3Row = Frame(content)
    alpha3Row.pack()
    a3Row = [26, 24, 3, 22, 2, 14, 13]
    finalButtonCount = populate_frame_buttons(alpha3Row, finalButtonCount, a3Row)

    #Create the prompt label
    label = Label(content, text=prompt, width=len(prompt), bg='light green')
    label.pack()


    #Binds all keys pressed to the on_key method
    label.bind_all('<Key>', on_key)

    load_sound_paths(sound_paths_file)

    #Tk's mainloop
    root.mainloop()

