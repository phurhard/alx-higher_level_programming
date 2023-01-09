def multiple_returns(sentence):
    if sentence == "":
        return None
    else:
        length = len(sentence)
        first_char = sentence[0]
        return (length, first_char)
