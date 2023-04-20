# ---------------------- New Game ---------------------- #
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter A, B, C or D: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guess)
# ---------------------- Checking options ---------------------- #
def check_answer(answer, guess):
    if answer == guess:
        print("Correct Answer !")
        return 1
    else:
        print("Wrong answer !")
        return 0
# ---------------------- Displaying Result ---------------------- #
def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("RESULTS")
    print("--------------------------------")

    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses / len(questions)*100)
    print("Your Score is: "+str(score)+"%")
# ---------------------- Play again ? ---------------------- #
def play_again():
    response = input("Do you want to play again? Y or N >> ")
    response = response.upper()

    if response == "Y":
        return True
    else: 
        return False
    
# ---------------------- Question set & Options ---------------------- #
questions = {
    "Who created Python? :": "A",
    "What year was python created? :": "B",
    "Who created C++ language? :": "C",
    "React belongs to which company? :": "A"
}

options = [["A. Guido Van Rossum", "B. Bill Gates", "C. Linus Torvalds", "D. James Gosling"],
          ["A. 1989", "B. 1991", "C. 1994", "D. 2001"],
          ["A. Dennis Ritchie", "B. James Gosling", "C. Bjarne Stroustrup", "D. Guido Van rossum"],
          ["A. Facebook", "B. Google", "C. Oracle", "D. Microsoft"]]

new_game()

while play_again():
    new_game()
print("See you again 👋🏻")
