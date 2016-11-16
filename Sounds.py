def key_pressed(button, key=None):
    if button is not None:
        key = button.id_string()

    if not edit_mode:
        if key.isnumeric():
            if sounds[int(key)] is not None:
                if repeating[int(key)] is False:
                    sounds[int(key)].play(-1)
                    repeating[int(key)] = True
                    buttons[int(key)].configure(bg="yellow")

                else:
                    repeating[int(key)] = False
                    sounds[int(key)].stop()
                    buttons[int(key)].configure(bg="light grey")
        elif key.isalpha():
            if sounds[ord(key) - 87] is not None:
                sounds[ord(key) - 87].stop()
                sounds[ord(key) - 87].play()
        else:
            if key.isnumeric():
                file = askopenfilename(filetypes=[("Sound files","*.wav")])

                try:
                    sounds[int(key)] = mixer.Sound(file)
                except:
                    print("Unable to load sound " + file)

                if sounds[int(key)] is not None:
                    paths[int(key)] = file
            elif key.isalpha():
                file = askopenfilename(filetypes=[("Sound files","*.wav")])

                try:
                    sounds[ord(key) - 87] = mixer.Sound(file)
                except:
                    print("Unable to load sounds " + file)

                if sounds[ord(key) - 87] is not None:
                    paths[ord(key) - 87] = file


def on_key(event):
        if event.char == event.keysym:
            
            key_pressed(None,event.char)