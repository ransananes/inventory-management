class TypeValidator:
    """
        Type Validator => validate data type
    """
    @staticmethod
    def validate_str(value, context=""):
        if not value or not isinstance(value, str):
            raise TypeError(f"{context} error: {value} must be a string.")

    @staticmethod
    def validate_integer(value, context=""):
        if not isinstance(value, int):
            raise TypeError(f"{context} error: {value} must be an integer.")

    @staticmethod
    def validate_num(value, context=""):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{context} error: {value} must be a number.")
        
