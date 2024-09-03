# Trivia Game - Glowing Five

# 💎

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Testing and Debugging Report](#testing-and-debugging-report)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This is a web-based quiz game built using Python and the Flask web framework. The game loads questions from a CSV file and presents them to the player one at a time. The player wins by correctly answering 5 questions before making 3 incorrect attempts.

## Features

- Multiple-choice questions loaded from a CSV file.
- Randomized question selection.
- Track of correct and incorrect answers.
- Win or lose the game based on player performance.
- Simple web interface with HTML forms.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Flask library for Python.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/alanmaizon/glowing-five.git
   cd glowing-five
   ```

2. Install required Python packages:

   ```bash
   pip install Flask
   ```

3. Place your CSV file with questions in the same directory as `app.py`. The CSV file should follow this structure:

   ```
   Question;Option1;Option2;Option3;Option4;CorrectAnswerIndex
   ```

   Example:

   ```
   When did the Berlin Wall fall?;1989;1988;1987;1990;1
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Open a web browser and navigate to `http://127.0.0.1:5000/` to start playing the game.

## Usage

- When you start the game, the first question will be displayed.
- Select the correct answer by clicking on the radio button and submit it.
- The game will display whether your answer is correct or incorrect.
- The game continues until you either answer 5 questions correctly or get 3 incorrect answers.

## File Structure

```
glowing-five/
│
├── app.py                # Main Flask application
├── modules.py            # Functions to create and edit CSV files
├── setup.py              # Setup for Win32
├── exceptions.py         # Functions to validate user interaction
├── validators.py         # Debugging tools to handle exceptions
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet for the app
│   ├── js/
│   │   └── timer.js      # JavaScript for frontend interactivity
│   ├── img/
│   │   └── logo.gif      # Main logo
│   ├── csv/
│   │   └── comedy.csv    # Quiz files
├── templates/
│   └── base.html         # Main HTML template
│   └── categories.html   # Select category HTML template
│   └── error.html        # Error HTML template
│   └── input_name.html   # Start input form HTML template
│   └── leaderboard.html  # Rank leader board HTML template
└── README.md             # This README file
```

## Testing and Debugging Report

### Testing

Testing was conducted manually by running the Flask application and performing the following actions:

1. **Correct Answers:**
   - Ensured that the correct count increases when a correct option is selected.
   - Verified that the game ends with a win after 5 correct answers.

2. **Incorrect Answers:**
   - Confirmed that the incorrect count increases when an incorrect option is selected.
   - Checked that the game ends with a loss after 3 incorrect answers.

3. **Question Randomization:**
   - Observed that the questions are presented in a random order.

4. **Form Submission:**
   - Ensured that the correct and incorrect results are displayed immediately after submission.
   - Verified that the form resets for the next question.

### Debugging

Several issues were identified and addressed during development:

1. **Incorrect display of questions and options** 
   - Ensured that the CSV file is read and parsed correctly, and that the HTML template receives the correct data structure.

2. **Game not resetting correctly after a win/loss** 
   - Added initialization of game state variables (`correct_count`, `incorrect_count`, `round`) in the `start_game` function.

3. **Form submission not correctly identifying the selected option.** 
   - Adjusted the HTML form to ensure that the selected option is passed correctly as a POST parameter.

4. **Incorrect game state tracking after form submission.** 
   - Verified the logic for updating the `correct_count` and `incorrect_count` to ensure the game progresses as expected.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the existing style and that you have tested your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
