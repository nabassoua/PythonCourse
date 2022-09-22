def entrelacement1(s1, s2):

    s = " "

    for i in range(len(s1)):
        s += s1[i] + s2[i]
    return s


print(entrelacement1('abc', '123'))