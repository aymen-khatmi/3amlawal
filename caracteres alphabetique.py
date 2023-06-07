ch=input("entrer une chaine de caractaire:")
ch2=""
for i in ch:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        ch2+=i

print(ch2)

