def parse_int(value:str) -> int |None:
        """
        Parse a string into an integer, throwing if it's not a valid int, or None if it's an empty string
        """
        return int(value) if len(value) > 0 else None

def parse_float(value:str) -> float |None:
        """
        Parse a string into an float, throwing if it's not a valid int, or None if it's an empty string
        """
        return float(value) if len(value) > 0 else None

def parse_boolean (value:str) -> bool | None:
        return True if int(value) > 0 else False