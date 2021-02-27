import re

def abbreviate(words):
    clean = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in words.split()]
    result = []
    for word in clean:
        if word == " ":
            word = ""
        result.append(word[0])
    return "".join(result).upper()
    