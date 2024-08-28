# validators.py

from exceptions import InvalidQuestionFormatError, InvalidAnswerFormatError

def validate_question_format(line, line_num):
    """
    Validate the format of the question.
    A valid question should have exactly 6 fields separated by a semicolon.
    """
    reg = line.replace("\n", "").split(";")
    if len(reg) != 6:
        raise InvalidQuestionFormatError(line_num)
    
    try:
        question = {
            "question": reg[0],
            "options": reg[1:5],
            "answer": int(reg[5])
        }
        return question
    except ValueError:
        raise InvalidAnswerFormatError(line_num)
