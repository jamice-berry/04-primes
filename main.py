from math import sqrt

#### Fonction secondaire


def isprime(p):
    if(p<= 0):
        return False
    
    a = p/2+1
    for i in range(2,p//2 +1):
        if(p%i == 0):
            print(f"{p} = {i} x {p // i} : False")
            return False
            
        
    print (p, ": True")
    return True


    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
