f1 = open('KLSadd_2.tex', 'r')
f2 = open('KLSadd_2-out.tex', 'w')
while 1:
    char = f1.read(1)
    if char and ord(char) >= 97 and ord(char) <= 122: # a - z
        f2.write(chr(ord(char)-32))
    elif char and ord(char) >= 65 and ord(char) <= 90: # A - Z
        f2.write(chr(ord(char)+32))
    else: f2.write(char)
    if not char: break
f1.close()
f2.close()
