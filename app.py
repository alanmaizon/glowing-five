from flask import Flask, request, render_template
import random as rn

app = Flask(__name__)

# Load questions from the CSV file
def load_questions(file_name):
    questions = []
    with open(file_name, "r") as f:
        for line in f:
            reg = line.strip().split(";")
            question = {
                "question": reg[0],
                "options": reg[1:5],
                "answer": int(reg[5])
            }
            questions.append(question)
    return questions


questions = load_questions("questions.csv")

# Initialize game variables
game_state = {
    "correct_count": 0,
    "incorrect_count": 0,
    "round": 0
}

@app.route("/")
def start_game():
    game_state["correct_count"] = 0
    game_state["incorrect_count"] = 0
    game_state["round"] = 0
    return ask_question()

@app.route("/question")
def ask_question():
    if game_state["correct_count"] >= 5:
        return render_template("base.html", game_over=True, won=True, round=game_state['round'])
    if game_state["incorrect_count"] >= 3:
        return render_template("base.html", game_over=True, won=False, round=game_state['round'])

    question = rn.choice(questions)
    game_state["round"] += 1

    # Pass the question, round, and enumerate to the template
    return render_template("base.html", game_over=False, question=question, round=game_state['round'], enumerate=enumerate)

@app.route("/answer", methods=["POST"])
def answer_question():
    selected_option = request.form.get("option")
    correct_answer = int(request.form["correct_answer"])
    correct_answer_text = request.form["correct_answer_text"]
    
    if selected_option is None:
        game_state["incorrect_count"] += 1
        return f"<h2>Time's up! The correct answer was '{correct_answer_text}'</h2>{ask_question()}"
    
    selected_option = int(selected_option)
    
    if selected_option == correct_answer:
        game_state["correct_count"] += 1
        return f"<h2>Correct!</h2>{ask_question()}"
    else:
        game_state["incorrect_count"] += 1
        return f"<h2>Incorrect! The correct answer was '{correct_answer_text}'</h2>{ask_question()}"

@app.route("/restart", methods=["POST"])
def restart_game():
    game_state["correct_count"] = 0
    game_state["incorrect_count"] = 0
    game_state["round"] = 0
    return start_game()

if __name__ == "__main__":
    app.run(debug=True)
