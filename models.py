import random as rn
from validators import validate_question_format
from exceptions import InvalidQuestionFormatError, InvalidAnswerFormatError

# Game state and user information
game_state = {
    "correct_count": 0,
    "incorrect_count": 0,
    "round": 0,
    "skips": 0,
    "user_name": "",
    "category": "",
    "asked_questions": []  # List to keep track of asked questions
}

leaderboard = []

def load_questions(file_name):
    questions = []
    encodings = ["utf-8", "latin-1"]

    for encoding in encodings:
        try:
            with open(file_name, "r", encoding=encoding) as f:
                for i, line in enumerate(f.readlines()):
                    if not line.strip():
                        continue
                    
                    try:
                        question = validate_question_format(line, i + 1)
                        questions.append(question)
                    except (InvalidQuestionFormatError, InvalidAnswerFormatError) as e:
                        print(e)  # Log the exception message
                        continue  # Skip the invalid question and continue
                    
            break  # Exit the loop if reading was successful
        except UnicodeDecodeError as e:
            print(f"Encoding {encoding} failed: {e}")
            continue  # Try the next encoding if the current one fails

    if not questions:
        print(f"Warning: No questions loaded from {file_name}")

    return questions

def select_random_question(questions, asked_questions):
    # Exclude already asked questions
    available_questions = [q for i, q in enumerate(questions) if i not in asked_questions]
    
    if not available_questions:
        return None
    
    selected_question = rn.choice(available_questions)
    asked_questions.append(questions.index(selected_question))
    
    return selected_question
