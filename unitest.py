import unittest
import exo

class TestExo1(unittest.TestCase):

    def test_fonction(self):
        self.assertEqual(exo.exercice_1(1,0), 0)
        self.assertEqual(exo.exercice_1(-2, 1.5), -3.0)
        self.assertRaises(TypeError, exo.exercice_1, 'a', 'b')
        self.assertRaises(TypeError, exo.exercice_1, 'a', 2)


class TestExo2(unittest.TestCase):

    def test_cas_1(self):
        self.assertEqual(exo.exercice_2(1,4,5), -255)
    def test_cas_2(self):
        self.assertEqual(exo.exercice_2(2,1,3), 2)
    def test_cas_3(self):
        self.assertEqual(exo.exercice_2(50, 1, 2), 255)

    def test_type(self):
        self.assertRaises(TypeError, exo.exercice_2, 'a', 2, 3)
        self.assertRaises(TypeError, exo.exercice_2, 1, 'b', 'ecf')
        self.assertRaises(TypeError, exo.exercice_2, 1, 2, 'ecf')
        self.assertRaises(TypeError, exo.exercice_2, 50, 'b', 1.5)


class TestExercice3(unittest.TestCase):


    def test_init(self):
        self.assertRaises(TypeError, exo.Exercice_3, 'a')
        self.assertRaises(ValueError, exo.Exercice_3, -2)

    def test_aire(self):
        cercle = exo.Exercice_3(1)
        self.assertEqual(cercle.aire(), 3.141592653589793)

    def test_perimetre(self):
        cercle = exo.Exercice_3(1)
        self.assertEqual(cercle.perimetre(), 6.283185307179586)




