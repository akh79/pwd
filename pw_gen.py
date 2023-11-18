# password generator

from random import randint
from random import choices
from random import shuffle
from sys    import exit

def passwordgen(n):

    consonant = "bcdfghjklmnpqrstvwxz"
    vowel = "aeiouy"
    digit = "0123456789"
    other = "_-!();:"
    
    if n < 8 :
        n = 8
    m = n//2 if n%2 == 0 else n//2+1

    pwlstc = choices(consonant, k=m)
    shuffle(pwlstc)
    pwlstv = choices(vowel, k=n-m)
    shuffle(pwlstv)

    pwlst = []
    for i in range(len(pwlstc)):
        pwlst.append(pwlstc[i])
        if i < len(pwlstv):
            pwlst.append(pwlstv[i])
    pwd = "".join(pwlst)
    return pwd

if __name__ == "__main__":
    try:
        ns = input("Enter password length: ")
        n = int(ns)
    except ValueError as e:
        print("Error: not an integer")
        exit(2)

    if n < 8:
        print("Entered length is below minimum of 8. Will be set to 8")

    pwd = passwordgen(n)
    print(pwd)


    
    
