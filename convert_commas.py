import csv

def convert_commas_to_semicolons(text: str) -> str:
    """
    Converts all commas in the input text to semicolons.

    Parameters:
    text (str): The input string containing commas.

    Returns:
    str: The string with commas replaced by semicolons.
    """
    return text.replace(',', ';')

input_file = 'input.csv'
output_file = 'output.csv'

# Read the input CSV and write to the output CSV with commas replaced by semicolons
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=';')

    for row in reader:
        # Convert each cell in the row from ',' to ';'
        converted_row = [convert_commas_to_semicolons(cell) for cell in row]
        
        # Write the converted row to the output file
        writer.writerow(converted_row)

print(f"Commas have been replaced with semicolons and saved to {output_file}.")
