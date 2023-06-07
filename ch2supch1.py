ch1=input("donner une chaine de caractere ch1:")
ch2=input("donner une chaine de caractere ch2:")

if len(ch1) > len(ch2):
    print("ch1 sup que ch2")
elif len(ch1) < len(ch2):
    print("ch2 sup que ch1")
else:
    print("ch1 egale ch2")
