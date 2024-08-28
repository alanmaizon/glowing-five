# exceptions.py

class InvalidQuestionFormatError(Exception):
    """Exception raised for errors in the question format."""
    def __init__(self, line_num, message="Invalid question format"):
        self.line_num = line_num
        self.message = f"{message} on line {line_num}"
        super().__init__(self.message)

class InvalidAnswerFormatError(Exception):
    """Exception raised for errors in the answer format."""
    def __init__(self, line_num, message="Answer must be an integer"):
        self.line_num = line_num
        self.message = f"{message} on line {line_num}"
        super().__init__(self.message)
