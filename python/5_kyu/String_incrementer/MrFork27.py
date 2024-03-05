def increment_string(string):
    number_position = len(string)
    string_result = string
    has_number = False

    for letter in string[::-1]:
        if letter.isnumeric() and not has_number:
            number_position = number_position - 1
        else:
            has_number = True

    if number_position != len(string):
        number_string = string[number_position:]
        number_incremented = str(int(number_string) + 1)
        string_incremented = "".join(
            "0" for i in range(len(number_string) - len(number_incremented))
        )
        string_result = (
            string_result[:number_position] + string_incremented + number_incremented
        )
    else:
        string_result = string_result + "1"

    return string_result
