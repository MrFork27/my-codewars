def order(sentence):
    order_sentence = [""] * len(sentence.split())

    for word in sentence.split():
        position = int(list(filter(lambda letter: letter.isnumeric(), word))[0])
        order_sentence[position - 1] = word

    return " ".join(word for word in order_sentence).strip()
