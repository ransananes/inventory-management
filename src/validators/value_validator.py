class ValueValidator:
    """
        Value Validator => validate data values
    """
    @staticmethod
    def validate_non_negative(value, context: str=""):
        if value < 0:
            raise ValueError(f"{context} error: {value} can't be negative.")
