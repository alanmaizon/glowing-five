# Trivia Game - Glowing Five

## Loading Questions:

The game loads questions from a CSV file named questions.csv. Each question has four possible answers, and one correct answer is identified by an index.

## Game Initialization:

The game initializes with zero correct and incorrect answers, and it starts at round 0.

## Game Flow:

### Start Game:
The game begins when the player accesses the root URL (/). This resets the game's state and presents the first question.

### Ask Question:
The game selects a random question from the loaded list and displays it to the player. The player is given four options to choose from.

### Submit Answer:
The player submits their selected answer via a form. The game then checks if the answer is correct or not.
If correct, the player's correct answer count increases by 1.
If incorrect, the incorrect answer count increases by 1.

## Winning and Losing Conditions:

The player wins if they answer 5 questions correctly before accumulating 3 incorrect answers.
A message is displayed indicating that the player has won, along with the round number in which the game was won.

The player loses if they reach 3 incorrect answers.
A message is displayed indicating that the player has lost, along with the round number in which the game was lost.

### Game Interface:

The game is presented in a simple HTML format where each question is displayed with radio buttons for the player to select their answer. A submit button sends the player's choice to the server.
