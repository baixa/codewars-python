def solution(s):
    result = ''
    for i in range(len(s)):
        if s[i].isupper():
            result += ' '
        result += s[i]
    return result
