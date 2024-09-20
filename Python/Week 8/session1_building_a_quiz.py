# WEEK 8: Building a Quiz with Python

# In this session, we will build a quiz using classes, lists, and loops!

# Step 1: Create a new file called 'question.py'
# This file will contain the Question class to handle the quiz questions.

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt  # The question prompt
        self.answer = answer  # The correct answer

# Step 2: Create a new file called 'quiz.py'
# This file will handle the quiz logic and user interaction.

from question import Question  # Importing the Question class

# List of question prompts
question_prompts = [
    "What colour are oranges?\n(a) Orange\n(b) Purple\n(c) Brown\n\n",
    "What colour are lions?\n(a) Black\n(b) Brown\n(c) Blue\n\n",
    "How many kilometers in a mile?\n(a) 2\n(b) 0.7\n(c) 1.6\n\n"
]

# Creating a list of Question objects
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

# Function to start the quiz
def start_quiz(questions):
    score = 0  # Initialize score
    for question in questions:
        answer = input(question.prompt)  # Prompt user for answer
        if answer.lower() == question.answer:  # Check if answer is correct
            score += 1  # Increment score for correct answer
    print(f"You got {score} out of {len(questions)}")  # Display final score

# Start the quiz
start_quiz(questions)

# Challenges
# Challenge 1: Add more questions to the quiz. You can use any topic you like!
# Challenge 2: Create a method in the Question class that prints the question and its possible answers.
# Challenge 3: Allow the user to retry the quiz and keep track of their best score.
# Challenge 4: Create a new class called 'Quiz' that holds the list of questions and the user's score.
# Challenge 5: Create a second quiz file that prompts users to create their own questions, answers, and then takes the quiz.

