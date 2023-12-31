import tkinter as tk
import json
import random

root = tk.Tk()

# Global Variables
categorylist = []
attempts = 6

# UI-Variables
colourmain = '#FBF7D7'
colouraccent = 'brown4'
# colourtext = '#4F372E'
colourhighlight = 'Grey'
colouractive = '#664F40'

fontheader = 'Baskerville Old Face', 45
fontmain = 'Baskerville Old Face', 30
fonthint = 'Baskerville Old Face', 15
fontsmall = 'Baskerville Old Face', 10

# Create transparent attribute for widgets
#root.wm_attributes('-transparent', '#ab23ff')

# root of game
root.geometry("800x800") # Sets the dimensions of the window size to be 800*800px
root.resizable(False, False) # Ensures that the game window is not resizable
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

def loseGame():
    clear_frame()

    loseText = tk.Label(
                root,
                fg = colouraccent,
                bg = colourmain,
                text = "YOU LOSE!\n RETRY?", 
                font = fontheader)
    
    back_button = tk.Button(
        root,
        fg=colouraccent,  # Text Colour
        bg=colourmain,  # Button Colour
        activeforeground=colouractive,
        activebackground=colourmain,
        border=1,
        text='Go Back',
        font=fontmain,
        command =  lambda: MainMenu()
    )

    back_button.focus()
    back_button.bind('<Return>', lambda event: MainMenu())
    back_button.place(x = 400, y = 600, anchor = 'center')
    loseText.place(x = 400, y = 400, anchor = 'center')
    
def nextGame(category, difficulty):
    clear_frame()
    print(len(categorylist))

    nextText = tk.Label(
                root,
                fg = colouraccent,
                bg = colourmain,
                text = "YOU WIN!\n READY FOR MORE?", 
                font = fontmain)
    
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
        command = lambda: Hangman(category, difficulty)
    )

    next_button.focus()
    next_button.bind('<Return>', lambda event: Hangman(category, difficulty))
    next_button.place(x = 400, y = 600, anchor = 'center')

def winGame(): 
    clear_frame()

    winText = tk.Label(
                root,
                fg = colouraccent,
                bg = colourmain,
                text = "YOU WIN!\n DO YOU WANT TO PLAY AGAIN?", 
                font = fontmain)
    
    #increase the size of the button
    winText.pack(expand = True, fill = 'both', side = tk.TOP)

    back_button = tk.Button(
        root,
        fg=colouraccent,  # Text Colour
        bg=colourmain,  # Button Colour
        activeforeground=colouractive,
        activebackground=colourmain,
        border=1,
        text='Go Back',
        font=fontmain,
        command = lambda: MainMenu()
    )

    back_button.focus()
    back_button.bind('<Return>', lambda event: MainMenu())
    back_button.place(x = 400, y = 600, anchor = 'center')


def hangmanGameLoop(wordToGuess, guessedWord, inputField, wordGuess, attempts_label, category, difficulty):
    global attempts
    print("hangmanGameLoop is active")
    
    #the letter that is guessed
    letterList = []
    wordToGuess_list = list(wordToGuess)

    guess = inputField.get()
    if guessedWord == wordToGuess_list: 
        nextGame(category, difficulty)
        if categorylist == []:
            winGame()
    elif "_" in guessedWord and attempts > 0:  
        if inputField not in letterList:
            letterList.append(guess)
            print(wordToGuess)
            if guess in wordToGuess:
                for i in range(len(wordToGuess)):
                    if guess == wordToGuess[i]:
                        # print(wordToGuess[i])
                        guessedWord[i] = guess
                        # print(guessedWord)
                    else:
                        print(wordToGuess[i])
                        # print("nopers")
            elif guess not in wordToGuess:
                attempts -= 1
                # print(attempts)
    elif attempts <= 0:
        loseGame()


    # Updates the wordGuess widget if you get an answer correct
    wordGuess.config(text = guessedWord)

    # Update attempts label
    attempts_label.config(text=f"Attempts Left: {attempts}")

    #deletes input after entering letter
    inputField.delete(0, 'end')


# Levels
def Hangman(category, difficulty):
    global attempts, categorylist
    clear_frame()
    
    # If there is nothing in categorylist, append all elements from category[difficulty] into categorylist
    if not categorylist:
        categorylist.extend(category[difficulty])
        
    # If category list exits, from category list, choose a random word & hint
    if categorylist:
        chosenList = random.choice(categorylist)
        categorylist.remove(chosenList)
        print(categorylist)
        wordToGuess, hintText = chosenList
        guessedWord = ["_"] * len(wordToGuess)
        for char in wordToGuess:
            if char == " ":
                space_index = wordToGuess.index(char)
                guessedWord[space_index] = " "
            elif char == "-":
                hyphen_index = wordToGuess.index(char)
                guessedWord[hyphen_index] = "-"
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
        command = lambda: hangmanGameLoop(wordToGuess, guessedWord, inputField, wordGuess, attempts_label, category, difficulty)
    )

    #binding the return/enter button
    inputField.bind('<Return>', lambda event: hangmanGameLoop(wordToGuess, guessedWord, inputField, wordGuess, attempts_label, category, difficulty))


    # UI Layout
    hint.place(x = 400, y = 200, anchor = 'center')
    # hint.pack(expand = True, fill = 'both', side = tk.TOP)
    inputField.place(x = 400, y = 600, anchor = 'center')
    wordGuess.place(x = 400, y = 350, anchor = 'center')
    attempts_label.place(x = 400, y = 450, anchor = 'center')
    enterInput.place(x = 400, y = 650, anchor = 'center')



# Difficulty Select Screen
def DifficultySelect(category):
    print(category)
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
        fg = '#37461E', # Text Colour
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
        fg = '#CD9B37', # Text Colour
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
        fg = '#BC622B', # Text Colour
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
        fg = '#8E4D63', # Text Colour
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
        fg = '#A74A43', # Text Colour
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
        fg = '#516067', # Text Colour
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
    global attempts
    clear_frame()

    if attempts != 6:
        attempts = 6

    print(categorylist)
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
        command = lambda: LevelSelect() 
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

    # UI Layout
    main_title.place(x = 400, y = 200, anchor = 'center')
    play.place(x = 400, y = 550, anchor = 'center')
    quitgame.place(x = 400, y = 650, anchor = 'center')

    
if __name__ == "__main__":
    MainMenu() # Upon running application, main menu screen is there
    root.mainloop()
