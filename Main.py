import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import json
import random

root = tk.Tk()

#global variable to keep track of the buttons pressed
pressed_buttons = []


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
#root.wm_attributes('-transparent', '#ab23ff')

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

attempts = 6

# Destroys all widgets under specified frame
# Referenced from https://stackoverflow.com/questions/70165908/how-to-switch-screens-using-tkinter
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

def loseGame():
    clear_frame()

    loseText = tk.Label(
                root,
                fg = colouraccent,
                bg = colourmain,
                text = "YOU LOSE!\n RETRY?", 
                font = fontheader)
    
    loseText.place(x = 400, y = 400, anchor = 'center')

def nextGame():
    clear_frame()

    nextText = tk.Label(
                root,
                fg = colouraccent,
                bg = colourmain,
                text = "YOU WIN!\n READY FOR MORE?", 
                font = fontheader)
    
    #increase the size of the button
    nextText.place(x = 400, y = 400, anchor = 'center')

    next_button = tk.Button(
        root,
        fg=colouraccent,  # Text Colour
        bg=colourmain,  # Button Colour
        activeforeground=colouractive,
        activebackground=colourmain,
        border=1,
        text='Next',
        font=fontmain,
        command =  lambda: restartHangman()
    )

    next_button.place(x = 400, y = 600, anchor = 'center')

# def winGame(): 
#     #same as next game but change the command to mainmenu()


def restartHangman():
    global pressed_buttons
    clear_frame()

    difficulty = pressed_buttons[1]
    category = pressed_buttons[2]
    Hangman(category, difficulty)
    pressed_buttons = []  # Reset pressed_buttons

def hangmanGameLoop(wordToGuess, guessedWord, inputField, wordGuess, attempts_label):
    global attempts, pressed_buttons
    print("hangmanGameLoop is active")
    
    #the letter that is guessed
    letterList = []
    wordToGuess_list = list(wordToGuess)
    

    guess = inputField.get()    
    if guessedWord == wordToGuess_list: 
        nextGame()
    elif "_" in guessedWord and attempts > 0:  
        if inputField not in letterList:
            print(attempts)
            letterList.append(guess)
            print(guess)
            print(wordToGuess)
            if guess in wordToGuess:
                for i in range(len(wordToGuess)):
                    if guess == wordToGuess[i]:
                        print(wordToGuess[i])
                        guessedWord[i] = guess
                        print(guessedWord)
                        print(attempts)
                    else:
                        print(wordToGuess[i])
                        print("nopers")
            elif guess not in wordToGuess:
                attempts -= 1
                print(attempts)
    elif attempts <= 0:
        loseGame()


    # Updates the wordGuess widget if you get an answer correct
    wordGuess.config(text = guessedWord)

    # Update attempts label
    attempts_label.config(text=f"Attempts Left: {attempts}")


# Levels
def Hangman(category, difficulty):
    global attempts, pressed_buttons
    clear_frame()
    
    # Creates a new category list and appends chosen category & difficulty from dictionary to list
    categorylist = [] 
    for item in category[difficulty]:
        categorylist.append(item)
    # word_list = category[difficulty]
    
    # From category list, choose a random word & hint
    chosenList = random.choice(categorylist)
    # chosenList = random.choice(word_list)
    categorylist.remove(chosenList)
    wordToGuess, hintText = chosenList
    guessedWord = ["_"] * len(wordToGuess)
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
    
    # Attempts Left
    attempts_label = tk.Label(
        root,
        fg=colouraccent,
        bg=colourmain,
        text=f"Attempts Left: {attempts}",
        font=fonthint
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
        #return into the terminal 
        command = lambda: hangmanGameLoop(wordToGuess, guessedWord, inputField, wordGuess, attempts_label)
    )

    #binding the return/enter button
    inputField.bind('<Return>', lambda event: hangmanGameLoop(wordToGuess, guessedWord, inputField, wordGuess, attempts_label))
        



    # UI Layout
    hint.place(x = 400, y = 200, anchor = 'center')
    # hint.pack(expand = True, fill = 'both', side = tk.TOP)
    inputField.place(x = 400, y = 600, anchor = 'center')
    wordGuess.place(x = 400, y = 350, anchor = 'center')
    attempts_label.place(x=400, y=450, anchor='center')
    enterInput.place(x = 400, y = 650, anchor = 'center')
    

# Difficulty Select Screen
def DifficultySelect(category):
    global pressed_buttons
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
        command = lambda: on_difficulty_selected(category, "easy")
        # command = lambda: Hangman(category, "easy") or pressed_buttons.append("easy")
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
        command = lambda: on_difficulty_selected(category, "medium")
        # command = lambda: Hangman(category, "medium") or pressed_buttons.append("medium")
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
        command = lambda: on_difficulty_selected(category, "hard")
        # command = lambda: Hangman(category, "hard")
        )
    
    # UI Layout
    diff_title.place(x = 400, y = 200, anchor = 'center')
    easy.place(x = 400, y = 400, anchor = 'center')
    medium.place(x = 400, y = 500, anchor = 'center')
    hard.place(x = 400, y = 600, anchor = 'center')

def on_difficulty_selected(category, difficulty):
    global pressed_buttons
    # selected_category = None
    # if category == "climate_change":
    #     selected_category = cc
    # elif category == "sustainability":
    #     selected_category = sus
    # elif category == "recycling":
    #     selected_category = rec

    # pressed_buttons.extend([difficulty, selected_category])
    # Hangman(selected_category, difficulty)
    pressed_buttons.extend([difficulty, category])
    Hangman(category, difficulty)
    
def LevelSelect():
    global pressed_buttons
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
        command = lambda: DifficultySelect(cc) or pressed_buttons.append("climate_change")
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
        command = lambda: DifficultySelect(sus) or pressed_buttons.append("sustainability")
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
        command = lambda: DifficultySelect(rec) or pressed_buttons.append("recycling")
        )
    
    # UI Layout
    level_title.place(x = 400, y = 200, anchor = 'center')
    climatechange.place(x = 400, y = 400, anchor = 'center')
    sustainability.place(x = 400, y = 500, anchor = 'center')
    recycling.place(x = 400, y = 600, anchor = 'center')



# Main Menu Screen
def MainMenu():
    global pressed_buttons
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
        command = lambda: LevelSelect() or pressed_buttons.append("play")
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

    print("Pressed Buttons:", pressed_buttons)
