"""
Script pour vérifier si un nombre entier est un nombre premier.

Ce fichier contient la définition de la fonction `isprime`, qui permet de déterminer
si un nombre donné est premier en le testant contre ses diviseurs possibles.
La fonction affiche également le résultat sous forme lisible, indiquant si le nombre
est premier ou, le cas échéant, un produit de deux facteurs.

Fonctions:
- isprime(p): Retourne True si le nombre est premier, False sinon, et imprime le résultat.

Exemples d'utilisation:
>>> isprime(11)
11: True

>>> isprime(12)
12 = 2 x 6 : False
"""
def isprime(p):
    """
    Détermine si un nombre entier donné est un nombre premier.

    Cette fonction prend en entrée un entier `p` et vérifie s'il est premier.
    Un nombre est premier s'il est supérieur à 1 et n'a aucun diviseur autre que 1 et lui-même.
    La fonction imprime également le résultat de l'opération.

    Parameters:
    p (int): Le nombre entier à tester.

    Returns:
    bool: True si le nombre est premier, False sinon.
    """
    if p <= 1:
        print(p, ": False")
        return False
    # La boucle ne vérifie que jusqu'à la moitié de p + 1
    a = p // 2 + 1
    for i in range(2, a):
        if p % i == 0:
            print(f"{p} = {i} x {p // i} : False")
            return False
    print(p, ": True")
    return True
