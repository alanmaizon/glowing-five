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
        return f"<h1>You've won in round {game_state['round']}</h1><p>GAME OVER</p>"
    if game_state["incorrect_count"] >= 3:
        return f"<h1>You've lost in round {game_state['round']}</h1><p>GAME OVER</p>"
    
    question = rn.choice(questions)
    game_state["round"] += 1
    
    html = f"""
    <h1>{question['question']}</h1>
    <form action="/answer" method="post">
        <input type="hidden" name="correct_answer" value="{question['answer']}">
        <input type="radio" name="option" value="1"> {question['options'][0]}<br>
        <input type="radio" name="option" value="2"> {question['options'][1]}<br>
        <input type="radio" name="option" value="3"> {question['options'][2]}<br>
        <input type="radio" name="option" value="4"> {question['options'][3]}<br>
        <input type="submit" value="Submit">
    </form>
    """
    return render_template_string(html)

@app.route("/answer", methods=["POST"])
def answer_question():
    selected_option = int(request.form["option"])
    correct_answer = int(request.form["correct_answer"])
    
    if selected_option == correct_answer:
        game_state["correct_count"] += 1
        return "<h2>Correct!</h2>" + ask_question()
    else:
        game_state["incorrect_count"] += 1
        return f"<h2>Incorrect! The correct answer was {correct_answer}</h2>" + ask_question()

if __name__ == "__main__":
    app.run(debug=True)
