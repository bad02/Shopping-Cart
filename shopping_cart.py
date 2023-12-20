class Product:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price


class ShoppingCart:
    def __init__(self, tax_rate=0.0):
        self.cart = {}
        self.tax_rate = tax_rate

    def add_product(self, product, quantity):
        if product.name not in self.cart:
            self.cart[product.name] = {"quantity": 0, "unit_price": product.unit_price}

        self.cart[product.name]["quantity"] += quantity

    def calculate_totals(self):
        total_price = sum(item["quantity"] * item["unit_price"] for item in self.cart.values())
        tax_amount = total_price * (self.tax_rate / 100)
        total_price_with_tax = total_price + tax_amount

        return round(total_price, 2), round(tax_amount, 2), round(total_price_with_tax, 2)


# Step 1
dove_soap = Product("Dove Soap", 39.99)
cart_step1 = ShoppingCart()
cart_step1.add_product(dove_soap, 5)
total_price_step1, _, _ = cart_step1.calculate_totals()
print(f"Step 1 - Total Price: {total_price_step1}")

# Step 2
cart_step2 = ShoppingCart()
cart_step2.add_product(dove_soap, 5)
cart_step2.add_product(dove_soap, 3)
total_price_step2, _, _ = cart_step2.calculate_totals()
print(f"Step 2 - Total Price: {total_price_step2}")

# Step 3
axe_deo = Product("Axe Deo", 99.99)
cart_step3 = ShoppingCart(tax_rate=12.5)
cart_step3.add_product(dove_soap, 2)
cart_step3.add_product(axe_deo, 2)
total_price_step3, tax_amount_step3, total_price_with_tax_step3 = cart_step3.calculate_totals()
print(f"Step 3 - Total Price: {total_price_step3}, Tax: {tax_amount_step3}, Total with Tax: {total_price_with_tax_step3}")