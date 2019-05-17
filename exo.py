import math

def exercice_1(a, b):
    """Fonction qui renvoie le produit de 2 nombres
    >>> exercice_1(2,3)
    6
    >>> exercice_1(2,4)
    8
    """
    if(type(a)) == str or type(b) == str:
        raise TypeError("Invalid argument")

    else:
        return a*b

def exercice_2(x, a, b):

    if x < a:
        if type(b) != int and type(b) != float:
            raise TypeError("Invalid argument")
        else:
            return -255
    elif x > b:
        if type(a) != int and type(a) != float:
            raise TypeError("Invalid argument")
        else:
            return 255
    else:
        return x


class Exercice_3:

    def __init__(self, r):

        if type(r) != int and type(r) != float:
            raise TypeError("Radius must be integers or float")
        elif r < 0:
            raise ValueError("Radius must be strictly positive")
        else:
            self.r = r

    def aire(self):

        return math.pi*self.r * self.r

    def perimetre(self):

        return 2 * math.pi * self.r

    def dans_cercle(self, x, y):

        norme = math.sqrt(x*x + y*y)

        if norme <= self.r:
            return True
        else:
            return False
