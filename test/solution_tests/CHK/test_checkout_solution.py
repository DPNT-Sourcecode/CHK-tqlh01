from solutions.CHK.checkout_solution import CheckoutSolution
import unittest

class TestCheckout(unittest.TestCase):
    def test_empty_cart(self):
        solution = CheckoutSolution()
        self.assertEqual(solution.checkout(""), 0)