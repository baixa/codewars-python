import re


def order(sentence):
    res = ["" for _ in range(10)]
    for i in sentence.split():
        res[int(re.search('\\d', i).group())] = i
    return " ".join(res).strip(" ")
