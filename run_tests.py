import unittest
from test_shopping_cart import TestShoppingCart

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestShoppingCart)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
