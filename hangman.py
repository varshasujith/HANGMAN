print("\n\n")
print("\t\t\t\t\t\t###################################### ")
print("\t\t\t\t\t\t######################################")
print("\t\t\t\t\t\t##                            ##                ")
print("\t\t\t\t\t\t##                            ##                ")
print("\t\t\t\t\t\t##                           0000               ")
print("\t\t\t\t\t\t##                          000000              ")
print("\t\t\t\t\t\t##                          000000              ")
print("\t\t\t\t\t\t##                           0000               ")
print("\t\t\t\t\t\t##                            ||                ")
print("\t\t\t\t\t\t##                          //||\\\             ")
print("\t\t\t\t\t\t##                         // || \\\            ")
print("\t\t\t\t\t\t##                            ||                ")
print("\t\t\t\t\t\t##                            ||                ")
print("\t\t\t\t\t\t##                            ||                ")
print("\t\t\t\t\t\t##                           _||_               ")
print("\t\t\t\t\t\t##                        //     \\\            ")
print("\t\t\t\t\t\t##                       //       \\\           ")
print("\t\t\t\t\t\t##                                              ")
print("\t\t\t\t\t\t===================                 ")
print("\t\t\t\t\t\t===================                 ")

print("\n\n\n\t\t\t\t\t\t\t\t\tWELCOME TO HANGMAN")

# CLUES

def clues(ch):
    if ch == 1:
        print("\t\t NUMBER OF LETTERS=6")
        print("\t\tCLUE 1- A PROGRAMMING LANGUAGE")
    elif ch == 2:
        print("\t\t NUMBER OF LETTERS=7")
        print("\t\tCLUE - KNOWN AS FATHER OF COMPUTER")
    elif ch == 3:
        print("\t\t NUMBER OF LETTERS=5")
        print("\t\tCLUE - PRESIDENT OF THE UNITED STATES")
    elif ch == 4:
        print("\t\tNUMBER OF LETTERS=6")
        print("\t\t CLUE - LEGENDARY BASKETBALL PLAYER WHO PLAYED FOR CHICAGO BULLS AS SHOOTING GUARD")
    elif ch == 5:
        print("\t\t NUMBER OF LETTERS=9")
        print("\t\tCLUE - MASTER BLASTER")
    elif ch == 6:
        print("\t\t NUMBER OF LETTERS=5")
        print("\t\tCLUE - WON 5 BALLON D'OR")
    elif ch == 7:
        print("\t\t NUMBER OF LETTERS=4")
        print("\t\tCLUE - PRIME MINISTER OF INDIA")
    elif ch == 8:
        print("\t\t NUMBER OF LETTERS=6")
        print("\t\tCLUE - OWNER OF RELIANCE PRIVATE LIMITED")
    elif ch == 9:
        print("\t\t NUMBER OF LETTERS=9")
        print("\t\tCLUE - OWNER OF MICROSOFT")
    elif ch == 10:
        print("\t\t NUMBER OF LETTERS=9")
        print("\t\tCLUE - OWNER OF APPLE INC.")

# HANGMAN SHAPES

def shapes(count):
    if count == 1:
        print('''
               '____
              |             |
              |             O
              |
              |
              |
              __''')
    elif count == 2:
        print('''
               '____
              |             |
              |             O
              |             |
              |             |
              |           
              __''')
    elif count == 3:
        print('''
               '____
              |             |
              |             O
              |            /|                
              |             |
              |
              __''')
    elif count == 4:
        print('''
               '____
              |             |
              |             O
              |            /|\\        
              |             |
              |
              __''')
    elif count == 5:
        print('''
               '____
              |             |
              |             O
              |            /|\\        
              |             |
              |             
              __''')
    elif count == 6:
        print('''
               '____
              |             |
              |             O
              |            /|\\        
              |             |
              |            / \\
              __''')

# FOR SINGLE PLAYER

def singleplayer():
    words = ["PYTHON", "BABBAGE", "TRUMP", "JORDAN", "TENDULKAR", "MESSI", "MODI", "AMBANI", "BILLGATES", "STEVEJOBS"]
    used = []  # USED LETTERS
    maxwrong = 7  # MAXIMUM NUMBER OF CHANCES
    count = 0
    choice = int(input("\nCHOOSE A NUMBER FROM 1 -10 TO SELECT A WORD: "))
    clues(choice)
    s1 = words[choice-1]
    s = list(s1)
    player = ["_ "] * len(s1)

    while count < maxwrong-1 and player != s:
        guess = input("\n\nENTER THE CHARACTER: ")
        if guess == '':
            print('Invalid input')
        elif guess.isalpha():
            guess = guess.upper()
            if guess not in used:
                if guess in s:
                    print("\nLETTER IS CORRECT")
                    used.append(guess)
                    for i in range(len(s1)):
                        if guess == s[i]:
                            player[i] = guess
                    print(" ".join(player))
                else:
                    print("\nINCORRECT")
                    count += 1
                    shapes(count)
            else:
                print("\nTHE LETTER IS ALREADY ENTERED!!!")
        else:
            print("\nPLEASE ENTER A VALID CHARACTER (ALPHABETS)!!!")

    if count < 6:
        print("\nCONGRATULATIONS YOU WON !!!! ")
        print("--------------------------------------------------------------")
    else:
        print("\nYOU LOST PLEASE TRY AGAIN !!!! ")
        print("--------------------------------------------------------------")

# INSTRUCTIONS

def steps():
    print("\n\n\t\t\t STEPS FOR SINGLEPLAYER")
    print("\t\t\t*************************************")
    print("\n\n STEP 1 - PLAYER 1 GETS A CHANCE TO CHOOSE A NUMBER BETWEEN 1 AND 10")
    print("\n\n STEP 2 - PLAYER 1 SHOULD TRY GUESSING THE LETTERS OF THE WORD")
    print("\n\n STEP 3 - IF THE CHARACTER ENTERED IS RIGHT THEN THE LETTER WILL BE FILLED IN THE BLANK SPACE")
    print("\n\n STEP 4 - IF THE CHARACTER ENTERED IS WRONG THEN THE HANGMAN SHAPE WOULD APPEAR")
    print("\n\n STEP 5 - PLAYER 1 CAN GUESS THE CHARACTERS TILL THE HANGMAN SHAPE IS COMPLETE")
    print("\n\n STEP 6 - ONCE THE HANGMAN SHAPE IS COMPLETE, THE GAME IS OVER")

    # STEPS FOR MULTIPLAYER
    print("\n\n\t\t\t STEPS FOR MULTIPLAYER")
    print("\t\t\t***********************************")
    print("\n\n STEP 1 - ENTER THE NAMES OF PLAYER 1 AND PLAYER 2")
    print("\n\n STEP 2 - PLAYER 1 GETS A CHANCE TO CHOOSE A NUMBER BETWEEN 1 AND 10")
    print("\n\n STEP 3 - PLAYER 1 SHOULD TRY GUESSING THE LETTERS OF THE WORD")
    print("\n\n STEP 4 - IF THE CHARACTER ENTERED IS RIGHT THEN THE LETTER WILL BE FILLED IN THE BLANK SPACE")
    print("\n\n STEP 5 - IF THE CHARACTER ENTERED IS WRONG THEN THE HANGMAN SHAPE WOULD APPEAR")
    print("\n\n STEP 6 - PLAYER 1 CAN GUESS THE CHARACTERS TILL THE HANGMAN SHAPE IS COMPLETE")
    print("\n\n STEP 7 - PLAYER 2 GETS A CHANCE TO CHOOSE A NUMBER FROM 1-10 EXCEPT THE NUMBER CHOSEN BY PLAYER 1")
    print("\n\n STEP 8 - PROCEED FROM STEP 3-6")
    print("\n\n STEP 9 - IF BOTH PLAYERS GUESS THE RIGHT ANSWER THEN THE PLAYER WHO MADE FEWER MISTAKES IS THE WINNER")
    print("\n\n STEP 10 - IF ANY PLAYER GUESSES THE RIGHT ANSWER, THAT PLAYER WINS")
    print("\n\n STEP 11 - IF BOTH PLAYERS FAIL TO GUESS THE WORD THEN BOTH PLAYERS LOSE")
    print("\n\n HOPE YOU UNDERSTOOD")
    print("-----------------------------------------------")
    print("\n\n")
    return main()

# FOR MULTIPLAYER

def multiplayer():
    player1 = input("\nENTER PLAYER 1 NAME: ").upper()
    player2 = input("\nENTER PLAYER 2 NAME: ").upper()
    print(f"\nWELCOME {player1} and {player2}")

    # Player 1's turn
    print(f"\n{player1}'S TURN")
    words = ["PYTHON", "BABBAGE", "TRUMP", "JORDAN", "TENDULKAR", "MESSI", "MODI", "AMBANI", "BILLGATES", "STEVEJOBS"]
    used = []  # USED LETTERS
    maxwrong = 7  # MAXIMUM NUMBER OF CHANCES
    count1 = 0
    chance = 0
    choice = int(input("\nCHOOSE A NUMBER FROM 1 -10 TO SELECT A WORD: "))
    clues(choice)
    s1 = words[choice-1]
    s = list(s1)
    player = ["_ "] * len(s1)

    while count1 < maxwrong-1 and player != s:
        guess = input("\n\nENTER THE CHARACTER: ")
        if guess == '':
            print('Invalid input')
        elif guess.isalpha():
            guess = guess.upper()
            if guess not in used:
                if guess in s:
                    print("\nLETTER IS CORRECT")
                    used.append(guess)
                    chance += 1
                    for i in range(len(s1)):
                        if guess == s[i]:
                            player[i] = guess
                    print(" ".join(player))
                else:
                    print("\nINCORRECT")
                    count1 += 1
                    chance += 1
                    shapes(count1)
            else:
                print("\nTHE LETTER IS ALREADY ENTERED!!!")
        else:
            print("\nPLEASE ENTER A VALID CHARACTER (ALPHABETS)!!!")

    if count1 < 6:
        print("\nCONGRATULATIONS YOU GOT THE RIGHT ANSWER !!!! ")
    else:
        print("\nYOU DID NOT GET THE RIGHT ANSWER !!!! ")
    print(f"\nNUMBER OF CHANCES TAKEN = {chance}")

    # Player 2's turn
    print(f"\n{player2}'S TURN")
    words = ["PYTHON", "BABBAGE", "TRUMP", "JORDAN", "TENDULKAR", "MESSI", "MODI", "AMBANI", "BILLGATES", "STEVEJOBS"]
    used = []  # USED LETTERS
    maxwrong = 7  # MAXIMUM NUMBER OF CHANCES
    count2 = 0
    chance = 0
    choice = int(input("\nCHOOSE A NUMBER FROM 1 -10 WHICH HAS NOT BEEN SELECTED BY PLAYER 1: "))
    clues(choice)
    s1 = words[choice-1]
    s = list(s1)
    player = ["_ "] * len(s1)

    while count2 < maxwrong-1 and player != s:
        guess = input("\n\nENTER THE CHARACTER: ")
        if guess == '':
            print('Invalid input')
        elif guess.isalpha():
            guess = guess.upper()
            if guess not in used:
                if guess in s:
                    print("\nLETTER IS CORRECT")
                    used.append(guess)
                    chance += 1
                    for i in range(len(s1)):
                        if guess == s[i]:
                            player[i] = guess
                    print(" ".join(player))
                else:
                    print("\nINCORRECT")
                    count2 += 1
                    chance += 1
                    shapes(count2)
            else:
                print("\nTHE LETTER IS ALREADY ENTERED!!!")
        else:
            print("\nPLEASE ENTER A VALID CHARACTER (ALPHABETS)!!!")

    if count2 < 6:
        print("\nCONGRATULATIONS YOU GOT THE RIGHT ANSWER !!!! ")
    else:
        print("\nYOU DID NOT GET THE RIGHT ANSWER !!!! ")
    print(f"\nNUMBER OF CHANCES TAKEN = {chance}")

    print("\t\t\t**************************************")
    if count1 < count2:
        print(f"\t\t\t\t\t{player1} WINS!!!")
    elif count2 < count1:
        print(f"\t\t\t\t\t{player2} WINS!!!")
    else:
        print("\t\t\t\t\tBOTH PLAYERS LOST!!!")
    print("\t\t\t************************************")

# MAIN OPTIONS

def main():
    print("\nOPTIONS ")
    print("\n1. SINGLE PLAYER")
    print("\n2. MULTIPLAYER")
    print("\n3. HOW TO PLAY")
    print("\n4. EXIT")
    
    ch = int(input("\nENTER THE CHOICE: "))
    if ch == 1:
        singleplayer()
    elif ch == 2:
        multiplayer()
    elif ch == 3:
        steps()
    elif ch == 4:
        print("\nHOPE YOU ENJOYED THE GAME")
        print("\nTHANK YOU AND HAVE A NICE DAY")
        exit()
    else:
        print("\nINVALID OPTION")
    
    k = input("\nWANT TO START A NEW GAME? (Y/N): ").upper()
    if k == 'Y':
        main()
    else:
        print("\nTHANK YOU FOR PLAYING HANGMAN")

main()
