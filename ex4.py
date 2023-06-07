ch2=""
for i in ch:
    ch2 = i + ch2
if ch == ch2:
    print(f"le mot {ch} est palindrome")
else:
    print(ch+ch2)




































'''
ch=input("donner une chaine de caracteres")
list1=[i for i in ch]

list2 = list1[::-1]

if list1 == list2:
    print(f"le mot {ch} est palindrome")
else:
    #print(f"le mot {ch} n'est pas palindrome")
    list3=list1+list2
    ch3=""
    for i in list3:
        ch3+=i
    print(ch3)



#version 2
'''
