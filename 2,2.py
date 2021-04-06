rez = -1
f = (['cobol', 1973, 'clips', 2011, 'oz'])
if f[2] == 'blade' and (rez == -1):
    rez = 11
if f[2] == 'clips' and (rez == -1):
    rez = 12

if rez == -1:

    if f[0] == 'cobol':
        if f[4] == 2014:
            rez = 1
        if f[4] == 1982:
            rez = 2
        if f[4] == 2011:
            rez = 3
    elif f[3] == 'blade' or f[3] == 'clips':

        rez = 10
    if f[0] == 'm':

        if f[4] == 'xojo':
            rez = 8
        if f[4] == 'oz':
            rez = 9
    elif f[3] == 'blade' or f[3] == 'clips':

        rez = 0

if f[0] == 1995:
    if f[4] == 2000:
        rez = 6
    if f[4] == 1997:
        rez = 7
    if f[4] == 1965:
        rez = 8
print(rez)
