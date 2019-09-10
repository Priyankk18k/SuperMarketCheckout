
class Checkout:
    class Discount:
        def __init__(self,nbritems,price):
            self.nbritems = nbritems
            self.price = price


    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}



    def addDiscount(self, item, nbrOfitems, price):
        discount = self.Discount(nbrOfitems,price)
        self.discounts[item] = discount

    # new_dict = {'A':{'nbritems': 2, 'price': 100},
    #     'A':{'nbritems': 3, 'price': 130},
    #     'A':{'nbritems': 4, 'price': 180},
    #     'A':{'nbritems': 5, 'price': 230},
    #     'A':{'nbritems': 6, 'price': 260},
    #     'B':{'nbritems': 6, 'price': 260}}


    def addItemPrice(self, item, price):
        self.prices[item] = price


    def addItem(self,item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1


    def calculateTotal(self):
        total = 0
        for item,count in self.items.items():
            total += self.CalculateItemTotal(item,count)
        return total


    def CalculateItemTotal(self,item,count):
        total = 0

        if item in self.discounts:
            discount = self.discounts[item]
            # print("Count",count)
            # print("Discount", discount.price)
            # print("itemsssssss",self.prices[item])
            if count >= discount.nbritems:
                total += self.CalculatedItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total


    def CalculatedItemDiscountedTotal(self, item, count, discount):
        total = 0
        noofdiscounts = count / discount.nbritems
        total += int(noofdiscounts) * discount.price
        remaining = count % discount.nbritems
        total += remaining * self.prices[item]
        return total
