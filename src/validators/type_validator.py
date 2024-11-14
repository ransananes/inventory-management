

class TypeValidator:
    """
        Type Validator 
            - validate_str => validate if value is string
            - validate_integer => validate if value is integer
            - validate_num => validate if value is a number (float/int)
    """
    @staticmethod
    def validate_str(value: str, context:str = ""):
        if not value or not isinstance(value, str):
            raise TypeError(f"{context} error: {value} must be a string.")

    @staticmethod
    def validate_integer(value: int, context:str = ""):
        if not isinstance(value, int):
            raise TypeError(f"{context} error: {value} must be an integer.")

    @staticmethod
    def validate_num(value, context:str = ""):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{context} error: {value} must be a number.")
        
