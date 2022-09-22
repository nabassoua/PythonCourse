def entrelacement1(s1, s2):

    s = " "

    for i in range(len(s1)):
        s += s1[i] + s2[i]
        print(s)
    return s


print(entrelacement1('abc', '123'))

# output
# a1
# a1b2
# a1b2c3
# a1b2c3