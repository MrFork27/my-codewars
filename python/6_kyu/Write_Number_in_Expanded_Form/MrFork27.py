def expanded_form(num):
    expanded_form_string = ""

    for index, digit in enumerate(str(num)):
        if int(digit) > 0:
            expanded_number = digit + "".join(
                "0" for i in range(index + 1, len(str(num)))
            )
            expanded_form_string = expanded_form_string + expanded_number + " + "

    return expanded_form_string[:-3]
