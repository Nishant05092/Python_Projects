questions =("1) How many bones are there in human body",
            "2) Hottest planet of solar system",
            "3) Total number of element in periodic table",
            "4) Which animal lays largest eggs",
            "5) Most abundant gas on earth atmosphere"
            )
options =(("A. 201","B. 202","C. 203","D. 206"),("A. Mercury","B. Venus","C. Earth","D. Mars")
          ,("A. 105","B. 110","C. 118","D. 119"),("A. hen","B. Crocodile","C. Whale","D. Ostrich"),
          ("A. Nitrogen","B. Hydrogen","C. Oxygen","D. LPG"))
answers =("D","B","C","D","A")
guesses =[]
Score =0
question_num =0
for question in questions:
    print(question)
    print("-----------------")
    for option in options[question_num]:
        print(option)
    guess = input("Enter: (A ,B ,C , D): ").upper()
    guesses.append(guess)
  
    if guesses[question_num] == answers[question_num]:
        print("---CORRECT---")
        Score += 1
    else:
        print("---INCORRECT---")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1    

print("----------------")
print("RESULT OF THE QUIZ")
print("----------------")
print("your answers")
for guess in guesses:
    print(guess,end=" ")
print()
print("Correct answers")
for answer in answers:
    print(answer,end=" ")
print()
print("---FINAL SCORE---")
final_score = int((Score/question_num)*100)
print(f"Your Score is {final_score}%")