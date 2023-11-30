import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import json
import random

root = tk.Tk()

# UI-Variables
colourmain = '#FFFFE4'
colouraccent = 'Brown'
colourhighlight = 'Grey'
colouractive = '#664F40'

fontheader = 'Comic Sans MS', 45
fontmain = 'Comic Sans MS', 30
fonthint = 'Comic Sans MS', 15
fontsmall = 'Comic Sans MS', 10

# Create transparent attribute for widgets
root.wm_attributes('-transparentcolor', '#ab23ff')

# root of game
root.geometry("800x800") # Sets the dimensions of the window size to be 800*800px
# root.resizable(False, False) # Ensures that the game window is not resizable
root.configure(bg = colourmain) # Sets background to off-white
root.title("Hangman")

# Dictionaries
ccfile = 'CC.txt'
with open(ccfile, 'r') as f:
    cc = json.load(f)

sustainabilityfile = 'SUSTAINABILITY.txt'
with open(sustainabilityfile, 'r') as f:
    sus = json.load(f)

recyclingfile = 'RECYCLING.txt'
with open(recyclingfile, 'r') as f:
    rec = json.load(f)

# Destroys all widgets under specified frame
# Referenced from https://stackoverflow.com/questions/70165908/how-to-switch-screens-using-tkinter
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def hangmanGameLoop(wordToGuess, guessedWord, attempts, inputField):

    print("hangmanGameLoop is active")

    letterList = []
    guess = inputField.get()

    if "_" in guessedWord and attempts > 0:
        if inputField not in letterList:
            letterList.append(guess)

            if guess in wordToGuess:
                for i in range(len(wordToGuess)):
                    if guessedWord[i] == guess:
                        guessedWord[i] = guess
            else:
                attempts -= 1

# Levels
def Hangman(category, difficulty):
    clear_frame()
    
    # Creates a new category list and appends chosen category & difficulty from dictionary to list
    categorylist = [] 
    for item in category[difficulty]:
        categorylist.append(item)
    
    # From category list, choose a random word & hint
    chosenList = random.choice(categorylist)
    categorylist.remove(chosenList)
    wordToGuess, hintText = chosenList
    guessedWord = ["_"] * len(wordToGuess)
    attempts = 6
    guess = ''

    inputField = tk.Entry(root,
                              border = 0,
                              fg = colouraccent,
                              bg = colourmain,
                              font = fontmain,
                              width = 1,
                              )
    inputField.focus()

    if len(inputField.get()) > 1:
        inputField.delete(1)
    
    # Hint Sentence
    hint = tk.Label(
                    root,
                    fg = colouraccent,
                    bg = colourmain,
                    text = hintText, 
                    font = fonthint
                    )
    
    # Guessed Word
    wordGuess = tk.Label(
                    root,
                    fg = colouraccent,
                    bg = colourmain,
                    text = guessedWord, 
                    font = fontmain
                    )
    
    enterInput = tk.Button(
        root, 
        fg = colouraccent, # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 1,
        text = 'enter', 
        font = fontsmall,
        command = lambda: hangmanGameLoop(wordToGuess, guessedWord, attempts, inputField)
        )

    # UI Layout
    # hint.place(x = 400, y = 200, anchor = 'center')
    hint.pack(padx = 10, pady = 100)
    inputField.place(x = 400, y = 600, anchor = 'center')
    wordGuess.place(x = 400, y = 350, anchor = 'center')
    enterInput.place(x = 400, y = 650, anchor = 'center')
    

# Difficulty Select Screen
def DifficultySelect(category):
    clear_frame()

    # Header
    diff_title = tk.Label(
                    root,
                     fg = colouraccent,
                     bg = colourmain,
                     text = "Difficulty Selection", 
                     font = fontheader)
    
    # Difficulty Selection Buttons
    easy = tk.Button(
        root, 
        fg = 'Green', # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'EASY', 
        font = fontmain,
        command = lambda: Hangman(category, "easy")
        )
    
    medium = tk.Button(
        root, 
        fg = 'Orange', # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'MEDIUM', 
        font = fontmain,
        command = lambda: Hangman(category, "medium")
        )
    
    hard = tk.Button(
        root, 
        fg = 'Red', # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'HARD', 
        font = fontmain,
        command = lambda: Hangman(category, "hard")
        )
    
    # UI Layout
    diff_title.place(x = 400, y = 200, anchor = 'center')
    easy.place(x = 400, y = 400, anchor = 'center')
    medium.place(x = 400, y = 500, anchor = 'center')
    hard.place(x = 400, y = 600, anchor = 'center')
    
def LevelSelect():
    clear_frame()

    # Header
    level_title = tk.Label(
                    root,
                     fg = colouraccent,
                     bg = colourmain,
                     text = "Level Select", 
                     font = fontheader
                     )
    
    # Category Selection Buttons
    climatechange = tk.Button(
        root, 
        fg = colouraccent, # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'CLIMATE CHANGE', 
        font = fontmain,
        command = lambda: DifficultySelect(cc)
        )
    
    sustainability = tk.Button(
        root, 
        fg = colouraccent, # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'SUSTAINABILITY', 
        font = fontmain,
        command = lambda: DifficultySelect(sus)
        )
    
    recycling = tk.Button(
        root, 
        fg = colouraccent, # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'RECYCLING', 
        font = fontmain,
        command = lambda: DifficultySelect(rec)
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
    main_title = tk.Label(
                    root,
                     fg = colouraccent,
                     bg = colourmain,
                     text = "HANGMAN\n(Environment Edition!)", 
                     font = fontheader
                    )

    # Main Menu Buttons
    play = tk.Button(
        root, 
        fg = colouraccent, # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'PLAY', 
        font = fontmain,
        command = LevelSelect
        )

    # Quit Game Button
    quitgame = tk.Button(
        root, 
        fg = colouraccent, # Text Colour
        bg = colourmain, # Button Colour
        activeforeground = colouractive,
        activebackground = colourmain,
        border = 0,
        text = 'QUIT', 
        font = fontmain,
        command = root.destroy # Force Quits Application
        )

    '''# Quit button with image placeholder
    global quit_button
    quit_button = PhotoImage(file='Images/QuitButton.png')
    quitgame = tk.Button(
        root, 
        image = quit_button,
        bg = colourmain,
        border = 0,
        command = root.destroy
        )'''

    # UI Layout
    main_title.place(x = 400, y = 200, anchor = 'center')
    play.place(x = 400, y = 550, anchor = 'center')
    quitgame.place(x = 400, y = 650, anchor = 'center')
    
if __name__ == "__main__":
    MainMenu() # Upon running application, main menu screen is there

root.mainloop()