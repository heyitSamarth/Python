class Checkout:
    def __init__(self):
        self.items={}
        self.total=0
    def add_item(self,item_name,item_price):
        self.items[item_name]=item_price
    def add_item_in_cart(self,item_name):
        self.total+=self.items[item_name]
    def calculate_total(self):
        return self.total
