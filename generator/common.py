import random
import string
import os.path

import jsonpickle

def randstr(prefix, maxlen, letters=True, digits=True, punctuation=True, spaces=True):
    symbols = ""
    if letters:     symbols += string.ascii_letters
    if digits:      symbols += string.digits
    if punctuation: symbols += string.punctuation
    if spaces:      symbols += " "*10
    return prefix + "".join (random.choice(symbols) for _ in range(random.randrange(maxlen))).strip()


def process_opts(n, f, opts):
    for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a
    
    return n, f


def write_json(path, testdata):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", path)

    with open(file, "w") as f:
        jsonpickle.set_encoder_options("json", indent=2)
        f.write(jsonpickle.encode(testdata))