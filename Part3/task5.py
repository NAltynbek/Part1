def twoStrings(s1, s2):
    new_s1 = s1.replace(' ','')
    new_s2 = s2.replace(' ','')
    for index in range(len(new_s1)):
        if new_s1[index] in new_s2:
            result = 'YES'
            break
        else:
            result = 'NO'
    return result
