import unittest

from shopping_cart import Product, ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.dove_soap = Product("Dove Soap", 39.99)
        self.axe_deo = Product("Axe Deo", 99.99)

    def test_step1(self):
        cart_step1 = ShoppingCart()
        cart_step1.add_product(self.dove_soap, 5)
        total_price_step1, _, _ = cart_step1.calculate_totals()
        self.assertEqual(total_price_step1, 199.95)

    def test_step2(self):
        cart_step2 = ShoppingCart()
        cart_step2.add_product(self.dove_soap, 5)
        cart_step2.add_product(self.dove_soap, 3)
        total_price_step2, _, _ = cart_step2.calculate_totals()
        self.assertEqual(total_price_step2, 319.92)

    def test_step3(self):
        cart_step3 = ShoppingCart(tax_rate=12.5)
        cart_step3.add_product(self.dove_soap, 2)
        cart_step3.add_product(self.axe_deo, 2)
        total_price_step3, tax_amount_step3, total_price_with_tax_step3 = cart_step3.calculate_totals()
        self.assertEqual(total_price_step3, 279.96)
        self.assertEqual(tax_amount_step3, 34.99)
        self.assertEqual(total_price_with_tax_step3, 314.95)

if __name__ == '__main__':
    unittest.main()
