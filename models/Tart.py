class Tart:
    def __init__(self, TartID, TartName, TartSize, TartPrice, TartQuantity,
                 OrderID, OrderDate, OrderTotal, OrderStatus):
        self.TartID = TartID
        self.TartName = TartName
        self.TartSize = TartSize
        self.TartPrice = TartPrice
        self.TartQuantity = TartQuantity
        self.OrderID = OrderID
        self.OrderDate = OrderDate
        self.OrderTotal = OrderTotal
        self.OrderStatus = OrderStatus
    def __str__(self):
        return (f'{self.TartID}\t{self.TartName}\t{self.TartSize}\t{self.TartPrice}\t{self.TartQuantity}\t'
                f'{self.OrderID}\t{self.OrderDate}\t{self.OrderTotal}\t{self.OrderStatus}')