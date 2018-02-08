class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def Sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        add_tax = self.price * tax
        self.price = self.price + add_tax
        return self
    def Return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "returned unopened":
            self.status = "for sale"
        if reason == "returned opened":
            discount = self.price * .2
            self.status = "used"
            self.price = self.price - discount
            return self
    def displayInfo(self):
        print "Price:", self.price
        print "Item name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

product1 = Product(100, "Expensive Shirt", 0.5, "Hugo Boss")
product1.Return("returned opened").displayInfo()

product2 = Product(900, "Suit", "3lbs", "Bonobos")
product2.addTax(.09).Sell().displayInfo()