import random
import string

def randstr(prefix, maxlen, letters=True, digits=True, punctuation=True, spaces=True):
    symbols = ""
    if letters:     symbols += string.ascii_letters
    if digits:      symbols += string.digits
    if punctuation: symbols += string.punctuation
    if spaces:      symbols += " "*10
    return prefix + "".join (random.choice(symbols) for _ in range(random.randrange(maxlen))).strip()