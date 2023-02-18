def nombre_apparitions(c, s):

    count = 0
    for i in range(len(s)):
        if s[i] == c:
            count += 1
    return count


def absence_de_e(s):

    return nombre_apparitions('e', s) == 0 and nombre_apparitions('E', s) == 0


print(absence_de_e('momP'))