def est_bien_ponctuee(s):

    for i in range(len(s)):
        if s[i] == '.':
            if s[i+1] == ' ':
                continue
            else:
                return False
    return True


print(est_bien_ponctuee('Un. Deux. '))