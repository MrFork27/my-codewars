def likes(names):
    likes_string = "no one likes this"
    names_len = len(names)

    if names_len == 1:
        likes_string = f"{names[0]} likes this"
    elif names_len == 2:
        likes_string = f"{names[0]} and {names[1]} like this"
    elif names_len == 3:
        likes_string = f"{names[0]}, {names[1]} and {names[2]} like this"
    elif names_len > 3:
        likes_string = f"{names[0]}, {names[1]} and {names_len - 2} others like this"

    return likes_string
