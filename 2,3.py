
tabl = [["+7 (092) 613‐47‐68", "+7 (092) 613‐47‐68", "Нет!17/11/2000"],
["+7 (713) 205‐16‐58", "+7 (713) 205‐16‐58", "Да!28/04/2004"],
["+7 (226) 136‐14‐90", "+7 (226) 136‐14‐90", "Да!20/01/2000"],
["+7 (245) 951‐21‐62", "+7 (245) 951‐21‐62 Д", "Да!03/10/2002"]]

def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]

    return res