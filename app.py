from flask import Flask, request, render_template, redirect, url_for
import random as rn
from validators import validate_question_format  # Import the validation function
from exceptions import InvalidQuestionFormatError, InvalidAnswerFormatError  # Import custom exceptions

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def input_name():
    if request.method == "POST":
        game_state["user_name"] = request.form.get("user_name")
        return redirect(url_for("select_category"))
    return render_template("input_name.html")

@app.route("/select_category", methods=["GET", "POST"])
def select_category():
    if request.method == "POST":
        game_state["category"] = request.form.get("category")
        return redirect(url_for("start_game"))
    return render_template("categories.html")

@app.route("/start_game")
def start_game():
    category_files = {
        "Entertainment": "static/csv/entertainment.csv",
        "Geography": "static/csv/geography.csv",
        "Comedy": "static/csv/comedy.csv",
        "Sports": "static/csv/sports.csv",
        "History": "static/csv/history.csv",
        "Science": "static/csv/science.csv",
        "Food": "static/csv/food.csv"
    }

    # Get the appropriate file based on the selected category
    questions_file = category_files.get(game_state["category"], "entertainment.csv")  # Fallback to "entertainment.csv"

    global questions
    questions = load_questions(questions_file)

    # Handle the case where no questions were loaded
    if not questions:
        return render_template("error.html", message="No valid questions found for this category. Please try another category.")

    # Reset game state
    game_state["correct_count"] = 0
    game_state["incorrect_count"] = 0
    game_state["round"] = 0
    game_state["skips"] = 0
    game_state["asked_questions"] = []  # Reset the list of asked questions
    return ask_question()

@app.route("/question")
def ask_question(message=None, message_type=None):
    if game_state["correct_count"] >= 5 or game_state["incorrect_count"] >= 3:
        result = "won" if game_state["correct_count"] >= 5 else "lost"
        leaderboard.append({
            "user_name": game_state["user_name"],
            "category": game_state["category"],
            "score": game_state["correct_count"],
            "round": game_state["round"],
            "skips": game_state["skips"]
        })
        leaderboard.sort(key=lambda x: (-x["score"], x["round"]))
        return render_template("base.html", message=f"You've {result}!", message_type=result, game_over=True, won=(result == "won"), round=game_state['round'], leaderboard=leaderboard, enumerate=enumerate, title="Game Over")

    available_questions = [q for i, q in enumerate(questions) if i not in game_state["asked_questions"]]

    if not available_questions:
        return render_template("error.html", message="No more questions available. Please restart the game.")

    selected_question = rn.choice(available_questions)
    game_state["asked_questions"].append(questions.index(selected_question))
    game_state["round"] += 1

    return render_template("base.html", message=message, message_type=message_type, game_over=False, question=selected_question, round=game_state['round'], enumerate=enumerate, title=f"Round {game_state['round']}")

@app.route("/answer", methods=["POST"])
def answer_question():
    selected_option = request.form.get("option")
    correct_answer = int(request.form["correct_answer"])
    correct_answer_text = request.form["correct_answer_text"]

    if selected_option is None:
        game_state["incorrect_count"] += 1
        return ask_question(message=f"Time's up! The correct answer was '{correct_answer_text}'", message_type="timeout")

    selected_option = int(selected_option)

    if selected_option == correct_answer:
        game_state["correct_count"] += 1
        return ask_question(message="Correct!", message_type="correct")
    else:
        game_state["incorrect_count"] += 1
        return ask_question(message=f"Incorrect! The correct answer was '{correct_answer_text}'", message_type="incorrect")

@app.route("/skip", methods=["POST"])
def skip_question():
    game_state["skips"] += 1
    return ask_question(message="Question skipped!", message_type="skip")

@app.route("/restart", methods=["POST"])
def restart_game():
    return redirect(url_for("select_category"))

@app.route("/leaderboard")
def show_leaderboard():
    return render_template("leaderboard.html", leaderboard=leaderboard, enumerate=enumerate)

if __name__ == "__main__":
    app.run(debug=True)