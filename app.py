from flask import Flask, request, render_template_string
import random as rn

app = Flask(__name__)

# Load questions from the CSV file
def load_questions(file_name):
    with open(file_name, "r") as f:
        questions = []
        for line in f.readlines():
            reg = line.replace("\n", "").split(";")
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
        return f"""
        <h1>You've won in round {game_state['round']}</h1>
        <p>GAME OVER</p>
        <form action="/restart" method="post">
            <input type="submit" value="Restart Game">
        </form>
        """
    if game_state["incorrect_count"] >= 3:
        return f"""
        <h1>You've lost in round {game_state['round']}</h1>
        <p>GAME OVER</p>
        <form action="/restart" method="post">
            <input type="submit" value="Restart Game">
        </form>
        """
    
    question = rn.choice(questions)
    game_state["round"] += 1
    
    # Convert the options to HTML form inputs
    options_html = ""
    for i, option in enumerate(question['options'], 1):
        options_html += f'<input type="radio" name="option" value="{i}"> {option}<br>'

    # Render the question and options with a timer
    html = f"""
    <h1>{question['question']}</h1>
    <p>Time left: <span id="timer">15</span> seconds</p>
    <form id="quiz-form" action="/answer" method="post">
        <input type="hidden" name="correct_answer" value="{question['answer']}">
        <input type="hidden" name="correct_answer_text" value="{question['options'][question['answer']-1]}">
        {options_html}
        <input type="submit" value="Submit">
    </form>
    """
    return render_template_string(html)


@app.route("/answer", methods=["POST"])
def answer_question():
    selected_option = request.form.get("option")
    correct_answer = int(request.form["correct_answer"])
    correct_answer_text = request.form["correct_answer_text"]
    
    if selected_option is None:
        # No option was selected, count as incorrect
        game_state["incorrect_count"] += 1
        return f"<h2>Time's up! The correct answer was '{correct_answer_text}'</h2>" + ask_question()
    
    selected_option = int(selected_option)
    
    if selected_option == correct_answer:
        game_state["correct_count"] += 1
        return "<h2>Correct!</h2>" + ask_question()
    else:
        game_state["incorrect_count"] += 1
        return f"<h2>Incorrect! The correct answer was '{correct_answer_text}'</h2>" + ask_question()


@app.route("/restart", methods=["POST"])
def restart_game():
    # Restart the game by resetting the game state and redirecting to the start
    game_state["correct_count"] = 0
    game_state["incorrect_count"] = 0
    game_state["round"] = 0
    return start_game()

if __name__ == "__main__":
    app.run(debug=True)
