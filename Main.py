import tkinter as tk
from tkinter import PhotoImage
import json
import random

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
wordfile = 'Wordbank.txt'
with open(wordfile, 'r') as f:
    wordbank = json.load(f)

# Destroys all widgets under specified frame
# Referenced from https://stackoverflow.com/questions/70165908/how-to-switch-screens-using-tkinter
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# Levels
def Levels(category, difficulty):
    clear_frame()
    # To place code for levels here

# Difficulty Select Screen
def DifficultySelect(category):
    clear_frame()

    # Header
    diff_title = tk.Label(root,
                     fg = accentcolour,
                     bg = maincolour,
                     text = "Difficulty Selection", 
                     font = (fontheader))
    
    # Difficulty Selection Buttons
    easy = tk.Button(
        root, 
        fg = 'Green', # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'EASY', 
        font = (mainfont),
        command = lambda: Levels(category, "easy")
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
        command = lambda: Levels(category, "medium")
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
        command = lambda: Levels(category, "hard")
        )
    
    # UI Layout
    diff_title.place(x = 400, y = 200, anchor = 'center')
    easy.place(x = 400, y = 400, anchor = 'center')
    medium.place(x = 400, y = 500, anchor = 'center')
    hard.place(x = 400, y = 600, anchor = 'center')
    
def LevelSelect():
    clear_frame()

    # Header
    level_title = tk.Label(root,
                     fg = accentcolour,
                     bg = maincolour,
                     text = "Level Select", 
                     font = (fontheader))
    
    # Category Selection Buttons
    climatechange = tk.Button(
        root, 
        fg = accentcolour, # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'CLIMATE CHANGE', 
        font = (mainfont),
        command = lambda: DifficultySelect("cc")
        )
    
    sustainability = tk.Button(
        root, 
        fg = accentcolour, # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'SUSTAINABILITY', 
        font = (mainfont),
        command = lambda: DifficultySelect("sus")
        )
    
    recycling = tk.Button(
        root, 
        fg = accentcolour, # Text Colour
        bg = maincolour, # Button Colour
        activeforeground = activecolour,
        activebackground = maincolour,
        border = 0,
        text = 'RECYCLING', 
        font = (mainfont),
        command = lambda: DifficultySelect("rec")
        )
    
    # UI Layout
    level_title.place(x = 400, y = 200, anchor = 'center')
    climatechange.place(x = 400, y = 400, anchor = 'center')
    sustainability.place(x = 400, y = 500, anchor = 'center')
    recycling.place(x = 400, y = 600, anchor = 'center')


# Main Menu Screen
def MainMenu():
    clear_frame()

    # Game Title
    main_title = tk.Label(root,
                     fg = accentcolour,
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
        command = LevelSelect
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
    main_title.place(x = 400, y = 200, anchor = 'center')
    play.place(x = 400, y = 550, anchor = 'center')
    quitgame.place(x = 400, y = 650, anchor = 'center')
    
if __name__ == "__main__":
    MainMenu() # Upon running application, main menu screen is there

root.mainloop()