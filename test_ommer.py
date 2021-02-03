import unittest
import ommer

class test_fam(unittest.TestCase):
    
    def test_ommer(self):
        """
        Test ommer function
        """
        test_range = 20
        test_cases = range(test_range)

        uncle = 'uncle'
        aunty = 'aunty'

        for n in test_cases:
            if (n != 0) and (n%3 == 0):
                self.assertIs(ommer.ommer(n), aunty)
            else:
                self.assertIs(ommer.ommer(n), uncle)