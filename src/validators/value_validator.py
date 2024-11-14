class ValueValidator:
    """
        Value Validator
            - validate_non_negative - validate if value is positive
    """
    @staticmethod
    def validate_non_negative(value, context: str=""):
        if value < 0:
            raise ValueError(f"{context} error: {value} can't be negative.")
