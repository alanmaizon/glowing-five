Here's an updated README for your trivia game, "Glowing Five," with more details about the game setup, functionality, and additional instructions:

---

# Trivia Game - Glowing Five

## Overview

"Glowing Five" is a web-based trivia game built using Flask. The game allows players to answer questions from different categories, track their scores, and see their standings on a leaderboard. The objective of the game is to answer 5 questions correctly before accumulating 3 incorrect answers.

## Features

- **Multiple Categories**: Choose from categories like Entertainment, Geography, Comedy, and more.
- **Dynamic Question Loading**: Questions are loaded dynamically from CSV files specific to each category.
- **No Repeated Questions**: Ensures that no question is repeated within a single game session.
- **Real-Time Feedback**: Players receive instant feedback on their answers.
- **Winning and Losing Conditions**: The game ends with a win or loss message based on the player's performance.
- **Leaderboard**: View the leaderboard to see top scores and track performance.
- **Responsive Design**: Works across various devices, including desktops, tablets, and mobile phones.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/alanmaizon/glowing-five.git
    cd glowing-five
    ```

2. **Install Dependencies**:
    Make sure you have Python 3.x installed. Install the required packages using `pip`:
    ```bash
    pip install flask
    ```

3. **Run the Application**:
    Start the Flask application:
    ```bash
    python app.py
    ```

4. **Access the Game**:
    Open your web browser and go to `http://127.0.0.1:5000/` to start the game.

## Game Flow

### 1. Start Game:
- The game begins by entering the player's name and selecting a category.
- The player accesses the chosen category via the URL `/select_category`.
- The first question is presented via the URL `/start_game`.

### 2. Ask Question:
- The game selects a random question from the loaded list for the chosen category and displays it to the player.
- The player is presented with four options and chooses their answer using radio buttons.

### 3. Submit Answer:
- The player submits their answer via a form.
- The game checks if the answer is correct:
  - If correct, the correct answer count increases by 1.
  - If incorrect, the incorrect answer count increases by 1.
  
### 4. Winning and Losing Conditions:

- **Winning**: The player wins by answering 5 questions correctly before accumulating 3 incorrect answers.
  - A message is displayed indicating the player has won, including the round number in which the game was won.
  
- **Losing**: The player loses if they reach 3 incorrect answers.
  - A message is displayed indicating the player has lost, including the round number in which the game was lost.

### 5. Game Over:
- When the game ends, the player is presented with options to restart the game or view the leaderboard.

## Game Interface

- The game is presented in a simple HTML format with:
  - Radio buttons for selecting answers.
  - A submit button to send the player's choice to the server.
  - Feedback messages indicating correct or incorrect answers, as well as win/lose status.

## Leaderboard

- The leaderboard displays the top scores with user names, scores, rounds, skips, and categories.
- Accessible via the "View Leaderboard" button when the game ends or through the `/leaderboard` URL.

## Error Handling

- The game gracefully handles errors such as:
  - Missing or malformed CSV files.
  - Unsupported file encodings.
  - Attempting to load questions from empty or incomplete lists.

## CSV File Format

Questions are loaded from CSV files, with each file corresponding to a category. The expected format for each line in a CSV file is:

```
Question;Option1;Option2;Option3;Option4;CorrectAnswerIndex
```

- **Example**:
  ```
  What is the capital of France?;Paris;Berlin;Madrid;Rome;1
  ```

Ensure the CSV files are correctly formatted and encoded in `utf-8` or `latin-1` to avoid loading issues.

## Development and Contribution

### Future Enhancements

- Add more categories and questions.
- Implement user authentication for personalized score tracking.
- Introduce difficulty levels and timed challenges.
- Improve error handling and logging for better diagnostics.

### Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues. Make sure to follow the standard guidelines for code style and testing.

## Testing

### Testing Plan

- Ensure all functionalities work as expected, including:
  - User registration and category selection.
  - Loading questions correctly from CSV files.
  - Tracking scores, rounds, and skips.
  - Displaying the leaderboard accurately.
  - Handling all edge cases, such as file errors and invalid inputs.

Use the browser's developer tools and Flask debugging mode to diagnose and fix any issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following this README, you will have a comprehensive understanding of how to set up, play, and contribute to the "Glowing Five" trivia game. Enjoy playing and developing!