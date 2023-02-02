"""
Denne funktion modtager to bogstaver og
returnerer det bogstav,
som kommer først i alfabetet.
Hvis bogstaverne er ens, returnerer
funktionen bogstav1.
Hvis parametrene er andet eller mere end et bogstav,
returnerer funktionen ingenting.
"""

def compareAlphabetically(bogstav1, bogstav2):
    # Fang ugyldige indtastninger
    if bogstav1.isalpha() and bogstav2.isalpha():
        if len(bogstav1) != 1 or len(bogstav2) != 1:
            return

        # Ensret for lettere sammenligning
        bogstav1 = str(bogstav1).lower()
        bogstav2 = str(bogstav2).lower()

        # Find det bogstav, som er først i alfabetet
        if ord(bogstav1) > ord(bogstav2):
            return bogstav2
        elif ord(bogstav1) < ord(bogstav2):
            return bogstav1
        else:
            return bogstav2

import unittest

class TestCompareFunction(unittest.TestCase):

    def testCompareAlphabetically(self):
        self.assertEqual(compareAlphabetically('a', 'b'), 'a')
        self.assertEqual(compareAlphabetically('b', 'a'), 'a')
        self.assertEqual(compareAlphabetically('A', 'B'), 'a')
        self.assertEqual(compareAlphabetically('B', 'A'), 'a')
        self.assertEqual(compareAlphabetically('a', 'B'), 'a')
        self.assertEqual(compareAlphabetically('A', 'b'), 'a')
        self.assertEqual(compareAlphabetically('b', 'A'), 'a')
        self.assertEqual(compareAlphabetically('B', 'a'), 'a')
        self.assertIsNone(compareAlphabetically('1', 'a'))
        self.assertEqual(compareAlphabetically('a', 'a'), 'a')
        self.assertEqual(compareAlphabetically('A', 'A'), 'a')
        self.assertIsNone(compareAlphabetically('a', '1'))
        self.assertIsNone(compareAlphabetically('a', 'testcase'))
        self.assertIsNone(compareAlphabetically('testcase', 'a'))
        self.assertEqual(compareAlphabetically('æ', 'å'), 'å')
        self.assertEqual(compareAlphabetically('z', 'å'), 'z')
        self.assertIsNone(compareAlphabetically('!', 'a'))

if __name__ == '__main__':
    unittest.main()
