from django.test import TestCase 

from suppliers.laskin import plus

class LaskinTests(TestCase):
    def test_plus(self):
        self.assertEqual(plus(3, 4), 7)
        self.assertEqual(plus(-3, 3), 0)
        self.assertEqual(plus(-3, -3), -6)
        self.assertEqual(plus(3.5, 2.5), 6.0)