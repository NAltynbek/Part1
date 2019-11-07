def countingValleys(n, s):
    valleys = 0
    position = 0
    for i in range(n):
        if position == -1 and s[i] == 'U':
           position += 1
           valleys += 1
        elif s[i] == 'D':
            position -= 1
        else:
            position += 1
    return valleys