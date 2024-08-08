class shopping_cart:
    def in_it(self,items):
        self.items = items


    def add_items(self,name,price):
        self.items[name] = price

    def remove_items(self name):