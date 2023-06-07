nb=int(input("entrer un nombre:"))

if nb > 1:
    for i in range(2,nb):
        if nb%i == 0:
            print("le nombre ne pas premier")
            break
    else:
        print("le nombre est premier")
else:
        print(f"le nomre {nb} ne pas premier")
