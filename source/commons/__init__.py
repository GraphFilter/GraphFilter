def calculate_string_difference(first_string: str, second_string: str) -> str:
    if second_string in first_string:
        return first_string.replace(second_string, '')
    if first_string in second_string:
        return second_string.replace(first_string, '')
    return first_string
