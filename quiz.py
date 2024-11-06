import random
import time

# Define your questions, options, answers, and hints
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A",
        "hint": "It's known as the City of Light.",
        "difficulty": "easy"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B",
        "hint": "It's an even number.",
        "difficulty": "easy"
    },
    {
        "question": "What color are bananas?",
        "options": ["A. Red", "B. Yellow", "C. Green", "D. Blue"],
        "answer": "B",
        "hint": "It's the color of the sun.",
        "difficulty": "easy"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C",
        "hint": "It's between 7 and 9.",
        "difficulty": "medium"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2", "B. H2O", "C. O2", "D. HO"],
        "answer": "B",
        "hint": "It contains two hydrogen atoms.",
        "difficulty": "medium"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Newton", "B. Einstein", "C. Tesla", "D. Galileo"],
        "answer": "B",
        "hint": "He had famously unruly hair.",
        "difficulty": "hard"
    },
]

# Function to save score history in a text file
def save_score(score):
    with open("score_history.txt", "a") as file:  # "a" mode appends to the file
        file.write(f"{score}\n")
    print("Your score has been saved!")

# Function to load and display score history from a text file
def load_score_history():
    try:
        with open("score_history.txt", "r") as file:
            scores = file.readlines()
            scores = [score.strip() for score in scores]
            print("Score History:", scores)
    except FileNotFoundError:
        print("No score history found.")

# Function to filter questions by difficulty level
def filter_questions(difficulty):
    return [q for q in questions if q["difficulty"] == difficulty]

# Main quiz game function with improvements
def quiz_game():
    print("Welcome to the Enhanced Quiz Game!")
    load_score_history()
    
    # Choose difficulty level
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    available_questions = filter_questions(difficulty)
    
    if not available_questions:
        print("No questions available for this difficulty level.")
        return
    
    # Shuffle questions
    random.shuffle(available_questions)
    
    # Set timer for each question
    time_limit = 10  # seconds per question
    score = 0
    
    for q in available_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        start_time = time.time()
        
        # Give the player a hint option
        use_hint = input("Do you want a hint? (y/n): ").lower()
        if use_hint == "y":
            print("Hint:", q["hint"])
        
        # Collect the answer
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        end_time = time.time()
        
        # Check if the answer is correct and within the time limit
        if end_time - start_time > time_limit:
            print("Time's up!")
        elif answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}")
        
        print(f"Time taken: {round(end_time - start_time, 2)} seconds")
    
    # Display final score and save it
    print(f"\nYour final score is {score}/{len(available_questions)}")
    save_score(score)

if __name__ == "__main__":
    quiz_game()
