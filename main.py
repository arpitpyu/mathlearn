import random

def multiplication_quiz():
    correct_answers = 0
    total_questions = 10

    print("Welcome to the multiplication quiz! Let's start:")
    
    for _ in range(total_questions):
        num1 = random.randint(3, 20)  # Random number between 3 and 20
        num2 = random.randint(1, 10)  # Random multiplier between 1 and 10
        answer = num1 * num2

        # Ask the question
        user_answer = int(input(f"What is {num1} x {num2}? "))
        
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Quiz completed! You got {correct_answers} out of {total_questions} correct.")

# Run the quiz
multiplication_quiz()


