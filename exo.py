import math
import requests

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

class Exercice 4:

    def __init__(self, title):

        self.URL = "https://fr.wikipedia.org/w/api.php"
        self.S = requests.Session()
        self.title = title

    def get_title(self):

        PARAMS = {
            'action': "query",
            'list': "search",
            'srsearch': self.title,
            'format': "json",
            'srlimit': 1
        }

        R = self.S.get(url=self.URL, params=PARAMS)
        DATA = R.json()

        return DATA["query"]["search"][0]["title"]

    def extract_info(self):

        title = self.get_title()

        PARAMS = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'titles': title,
            'explaintext': True,
            "exlimit": 1,
            'exchars': 175
        }

        R = self.S.get(url=self.URL, params=PARAMS)
        DATA2 = R.json()

        for elt in DATA2["query"]["pages"].values():
            return elt["extract"]
