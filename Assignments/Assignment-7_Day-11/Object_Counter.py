class Product:
    total_products = 0    # class attribute — shared counter

    def __init__(self, name, price, category):
        # your code here — also increment total_products
        self.name = name
        self.price = price
        self.category = category
        Product.total_products = Product.total_products + 1

    def display(self):
        # print product details using an f-string
        print(f"{self.name}, {self.price}, {self.category}")
	
print(Product.total_products)    # 0

p1 = Product('Laptop', 75000, 'Electronics')
p2 = Product('Shoes',   3000, 'Footwear')
p3 = Product('Coffee',    500, 'Beverages')

print(Product.total_products)    # 3
print(p1.total_products)         # 3 — accessible via object too
p1.display()
p2.display()
p3.display()
