from preloaded import MORSE_CODE


def decode_morse(morse_code):
    decode_string = ""

    for word in morse_code.strip().split("   "):
        for character in word.split(" "):
            decode_string = decode_string + MORSE_CODE[character]
        decode_string = decode_string + " "

    return decode_string.strip()
