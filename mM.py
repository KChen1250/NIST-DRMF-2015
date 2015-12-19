f1 = open('KLSadd.tex', 'r')
f2 = open('KLSadd-out.tex', 'w')
while 1:
    char = f1.read(1)
    if char == 'M':char = 'm'
    elif char == 'm':char = 'M'
    if not char: break
    f2.write(char)
f1.close()
f2.close()
