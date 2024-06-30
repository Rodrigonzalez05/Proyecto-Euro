class Restaurant:

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def show_products(self):
        for product in self.products:
            print(product.show_attr())

    def show_attr(self):

        print(f'''

Name: {self.name}
Products: 
        ''')

        self.show_products()