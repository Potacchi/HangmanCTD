import tkinter as tk
from tkinter import PhotoImage
import json

root = tk.Tk()

# UI-Variables
maincolour = '#FFFFE4'
accentcolour = 'Brown'
highlightcolour = 'Grey'
activecolour = '#664F40'

fontheader = 'Comic Sans MS', 45
mainfont = 'Comic Sans MS', 30

# root of game
root.geometry("800x800") # Sets the dimensions of the window size to be 800*800px
root.resizable(False, False) # Ensures that the game window is not resizable
root.configure(bg = maincolour) # Sets background to off-white
root.title("Hangman")

# Dictionaries
'''with open("Words.txt", encoding = 'utf-8') as f:
    wordbank = json.load(f)
print(wordbank)'''

# Destroys all widgets under specified frame
# Referenced from https://stackoverflow.com/questions/70165908/how-to-switch-screens-using-tkinter
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# Level Select Screen
def LevelSelect():
    clear_frame()

    # Header
    title = tk.Label(fg = accentcolour,
                     bg = maincolour,
                     text = "Level Select", 
                     font = (fontheader))
    
    # Level Select Buttons
    easy = tk.Button(
        root, 
        fg = 'Green', # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'EASY', 
        font = (mainfont),
        command = EasyLevel
        )
    
    medium = tk.Button(
        root, 
        fg = 'Orange', # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'MEDIUM', 
        font = (mainfont),
        # command = EasyLevel
        )
    
    hard = tk.Button(
        root, 
        fg = 'Red', # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'HARD', 
        font = (mainfont),
        # command = EasyLevel
        )
    
    # UI Layout
    title.place(x = 400, y = 200, anchor = 'center')
    easy.place(x = 400, y = 400, anchor = 'center')
    medium.place(x = 400, y = 500, anchor = 'center')
    hard.place(x = 400, y = 600, anchor = 'center')
    
# Main Menu Screen
def MainMenu():
    clear_frame()

    # Game Title
    title = tk.Label(fg = accentcolour,
                     bg = maincolour,
                     text = "HANGMAN\n(Environment Edition!)", 
                     font = (fontheader))

    # Main Menu Buttons
    play = tk.Button(
        root, 
        fg = accentcolour, # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'PLAY', 
        font = (mainfont),
        command = LevelSelect,
        )
    
    quitgame = tk.Button(
        root, 
        fg = accentcolour, # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'QUIT', 
        font = (mainfont),
        command = root.destroy # Force Quits Application
        )

    # UI Layout
    title.place(x = 400, y = 200, anchor = 'center')
    play.place(x = 400, y = 550, anchor = 'center')
    quitgame.place(x = 400, y = 650, anchor = 'center')

# Levels/Category
def Levels():
    clear_frame()
    # To place code for levels here
    text = 'placeholder'

def EasyLevel():
    clear_frame()

    global my_image
    my_image = PhotoImage(file="Images/test.png")
    test = tk.Label(root, image = my_image)
    test.place(x = 400, y = 400, anchor = 'center')

medium = 'placeholder'
hard = 'placeholder'

def Hangman():
    words = open('words.txt', 'r')
    

MainMenu() # Upon running application, main menu screen is there

root.mainloop()