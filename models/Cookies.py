class Cookies:
    def __init__(self, CookiesID, CookiesName, CookiesSize, CookiesPrice, CookiesQuantity,
                 OrderID, OrderDate, OrderTotal, OrderStatus):
        self.CookiesID = CookiesID
        self.CookiesName = CookiesName
        self.CookiesSize = CookiesSize
        self.CookiesPrice = CookiesPrice
        self.CookiesQuantity = CookiesQuantity
        self.OrderID = OrderID
        self.OrderDate = OrderDate
        self.OrderTotal = OrderTotal
        self.OrderStatus = OrderStatus
    def __str__(self):
        return (f'{self.CookiesID}\t{self.CookiesName}\t{self.CookiesSize}\t{self.CookiesPrice}\t'
                f'{self.CookiesQuantity}\t{self.OrderID}\t{self.OrderDate}\t{self.OrderTotal}\t{self.OrderStatus}')