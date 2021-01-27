def is_isogram(string):
    strip = ''.join([char for char in string if char.isalpha()])
    return len(strip.casefold()) == len(set(strip.casefold()))
