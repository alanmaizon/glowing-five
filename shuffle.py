import csv
import random

input_file = 'input.csv'
output_file = 'output.csv'

# Read the CSV file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')

    for row in reader:
        # Extract question, correct answer, incorrect answers, and the original position
        question = row[0]
        correct_answer = row[1]
        incorrect_answers = row[2:len(row) - 1]
        original_position = int(row[-1])

        # Combine all answers
        all_answers = incorrect_answers + [correct_answer]

        # Shuffle the answers
        random.shuffle(all_answers)

        # Find the new position of the correct answer
        updated_position = all_answers.index(correct_answer) + 1

        # Write the updated row to the new CSV file
        writer.writerow([question] + all_answers + [updated_position])

