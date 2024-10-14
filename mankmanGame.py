import random

words = ("apple","orange","chiku","pear",'banana', 'grapes',  'cherry', 'berry', 'watermelon', 'strawberries','avacado','mango', 'papaya','peach', 'plum','dates')

word_art = {
   0 : ("   ",
        "   ",
        "   " ),
   1 : (" o ",
        "   ",
        "   "),
   2 : (" o ",
        " | ",
        "   "),
   3 : (" o ",
        "/| ",
        "   "),
   4 : (" o ",
        "/|\\",
        "   "),
   5 : (" o ",
        "/|\\",
        "/  "),
   6 : (" o ",
        "/|\\",
        "/ \\")          
                           
}
def display_man(wrong_guess):
 print("****************")     
 for line in word_art[wrong_guess]:
     print(line)
 print("****************")  
def display_hint(hint):
    print(" " .join(hint))

def display_ans():
 
    print("**Congratulations you won the Game")

def main():
    answer =random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guess = 0
    guessed_letter = set()
    is_running = True

    while is_running:
     display_man(wrong_guess)
     
     display_hint(hint)
     guess =input("Guess a letter: ").lower()
     if len(guess)!= 1 or not guess.isalpha():
          print("invalid input")
          continue
     if guess in guessed_letter:
         print(f"{guess} is already guessed")

     guessed_letter.add(guess)

     if guess in answer:
          for i in range(len(answer)):
               if answer[i]==guess:
                    hint[i]=guess
     
     else:
         wrong_guess+=1
     
     if wrong_guess == 6:
         display_man(wrong_guess)
         print("you lose the game")
         print(f"Correct word is: {answer}")
         is_running = False
     if "_" not in hint:
         display_hint(hint)
         display_ans()
         is_running = False
 

if __name__ == "__main__":
    main()
    