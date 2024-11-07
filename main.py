
"""
Script pour tester la primalité de nombres entiers et afficher les nombres premiers 
dans une plage donnée.

Ce fichier contient deux fonctions :
- `isprime`: Fonction secondaire qui vérifie si un nombre donné est un nombre premier.
- `main`: Fonction principale qui teste la primalité de nombres dans une plage de 0 à 99
  et affiche les nombres premiers sous forme de liste.

Fonctions:
- isprime(p): Retourne True si le nombre `p` est premier, False sinon, et imprime le résultat.
- main(): Exécute une boucle de 0 à 99, teste la primalité de chaque nombre avec `isprime`,
  et affiche les nombres premiers trouvés.

Exemples d'utilisation:
Lorsque le script est exécuté directement, il affiche les nombres premiers de 0 à 99 :
>>> python script.py
2: True
3: True
...
97: True
Nombres premiers de 0 à 99 : 2, 3, 5, 7, 11, 13, ..., 97

"""
#### Fonction secondaire
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

#### Fonction principale


def main():
    """
    Fonction principale du script qui teste la primalité des nombres entiers de 0 à 99
    et affiche les nombres premiers trouvés.

    La fonction parcourt les entiers de 0 à 99 et utilise la fonction `isprime` pour
    vérifier si chaque nombre est premier. Si le nombre est premier, il est affiché
    en ligne, séparé par des virgules.

    Returns:
    None
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
