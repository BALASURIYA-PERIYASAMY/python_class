class Product:
    total_products = 0

    def __init__(self, name, price, category):
        self.name     = name
        self.price    = price
        self.category = category
        Product.total_products += 1

    @classmethod
    def create_discounted(cls, name, original_price, discount, category):
        # calculate discounted price and return a new Product object
        final_price = original_price - discount
        return cls(name, final_price, category)

    @classmethod
    def create_premium(cls, name, base_price, category):
        # prefix name with 'Premium ' and multiply price by 1.5
        # return a new Product object
        return cls('Premium ' + name, base_price * 1.5, category)

    @staticmethod
    def is_affordable(price):
        # return True if price is below 5000, else False
        return price < 5000

    def display(self):
        print(f'{self.name} | ₹{self.price} | {self.category}')

# Test:
p1 = Product('Laptop', 75000, 'Electronics')
p2 = Product.create_discounted('Shoes', 5000, 1000, 'Footwear')
p3 = Product.create_premium('Coffee', 400, 'Beverages')

p1.display()   # Laptop | ₹75000 | Electronics
p2.display()   # Shoes | ₹4000 | Footwear
p3.display()   # Premium Coffee | ₹600.0 | Beverages

print(Product.is_affordable(3000))   # True
print(Product.is_affordable(80000))  # False
