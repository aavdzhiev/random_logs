import re
from random import choice


def random_sentence():
    sentences = []
    for i in range(23):
        with open('kafka.txt'.format(i)) as f:
            sentences += re.findall(r".*?[\.\!\?]+", f.read())

    return choice(sentences)
