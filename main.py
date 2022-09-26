import wordslist,random,images
wordslist1,wordslist2,wordslist3=wordslist.manga_list,wordslist.marvel_list,wordslist.number_list
words1= wordslist1[1:-1].split()
words2= wordslist2[1:-1].split()
words3= wordslist3[1:-1].split()


number_words,marvel_words,manga_words=[],[],[]
for i in words1:
    manga_words.append(i)
for i in words2:
    marvel_words.append(i)
for i in words3:
    number_words.append(i)

print("lets play the hangman game")

def choose_difficulty():      
    print("please choose the level of difficulty: ","\n1. Easy","\n2. Medium","\n3. Hard")   
    level=input("enter your choice: ")
    choose_word(level)


def play_game(this_word,guesses):
    guessed=[]
    word=list(this_word)
    blanks="_" *len(word)
    blanks=list(blanks)
    for i in range(guesses):
        print(images.hangman[i])
        print("\nYou have {} chances left.".format(guesses),"\nYour word: " + " ".join(blanks),"\nGuessed letters: "," ".join(guessed))
        letter=input("your guess: ").lower()
        if len(letter)==1 and letter.isalpha():
            if letter in guessed:
                print("you already guessed that")
            elif letter in word:
                for index,character in enumerate(word):
                    blanks=list(blanks)
                    if character==letter:
                        blanks[index]=letter
                        current="".join(blanks)
                if blanks==word:
                    print("congratulations!! you won!!","\nYour word was","".join(word))
                    break
                    
                    
            elif letter not in word:
                guesses-=1
                guessed.append(letter)
                        
            else:
                print("only single letters allowed")
    else:
        print(images.hangman[7])
        print("sorry your game is over","\nyour word was","".join(word))
        play_again()

def hints(word):
    if word=="naruto":
        print("hint: I'm the nine tailed fox")
    elif word=="tsunade":
        print("hint: I'm one of the legendary")
    elif word=="sasuke":
        print("hint: I'm naruto's only rival")
    elif word=="itachi":
        print("hint: I'm sasuke's hatred.")
    elif word=="hinata":
        print("hint: I'm naruto's wife")
    elif word=="boruto":
        print("hint: I'm naruto's son")
    else:
        print("hint: I'm from shikamaru's team")

def choose_word(choice):
    if choice=="1":
        word=random.choice(number_words)
        print("\nhint: I'm every where in math textbook! yay!!")   
        play_game(word,6)
    elif choice=="2":
        guesses=7
        word=random.choice(marvel_words) 
        play_game(word,7)   
    else:
        guesses=8
        word=random.choice(manga_words)
        hints(word)
        play_game(word,8)


def play_again():
    """Offer the player a chance to play again."""
    repeat = input("Would you like to play again?[Y/N]\n>").lower()
    if repeat == 'y':
        print("Let's play!")
        choose_difficulty()
    else:
        print("Thanks for playing! Have a great day!")
        
difficulty=choose_difficulty()
