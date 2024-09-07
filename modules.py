# Module 3 - Python - UCD Professional Academy - Alan Maizon

import csv
import random

def convert_commas_to_semicolons(text: str) -> str:
    """
    Converts all commas in the input text to semicolons.

    Parameters:
    text (str): The input string containing commas.

    Returns:
    str: The string with commas replaced by semicolons.
    """
    return text.replace(',', ';')

def process_csv(input_file: str, output_file: str):
    """
    Converts commas to semicolons in the input CSV file and shuffles the answers.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file with processed data.
    """
    # Step 1: Convert commas to semicolons and save to a temporary file
    temp_file = 'temp.csv'
    with open(input_file, 'r') as infile, open(temp_file, 'w', newline='') as tempfile:
        reader = csv.reader(infile)
        writer = csv.writer(tempfile, delimiter=';')

        for row in reader:
            # Convert each cell in the row from ',' to ';'
            converted_row = [convert_commas_to_semicolons(cell) for cell in row]
            # Write the converted row to the temporary file
            writer.writerow(converted_row)

    # Step 2: Read the temporary file and shuffle the answers, then write to the final output file
    with open(temp_file, 'r') as tempfile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(tempfile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        for row in reader:
            # Ensure the row has enough elements to process
            if len(row) < 3:  # At least 1 question, 1 correct answer, and 1 position
                print(f"Skipping row due to insufficient data: {row}")
                continue
            
            # Extract question, correct answer, incorrect answers, and the original position
            question = row[0]
            correct_answer = row[1]
            incorrect_answers = row[2:- 1]
            original_position = int(row[-1])

            # Combine all answers
            all_answers = incorrect_answers + [correct_answer]

            # Shuffle the answers
            random.shuffle(all_answers)

            # Find the new position of the correct answer
            updated_position = all_answers.index(correct_answer) + 1

            # Write the updated row to the new CSV file
            writer.writerow([question] + all_answers + [updated_position])

    print(f"CSV processing completed. The output is saved to {output_file}.")

# Define file paths
input_file = 'input.csv'
output_file = 'output.csv'

# Process the CSV file
process_csv(input_file, output_file)
