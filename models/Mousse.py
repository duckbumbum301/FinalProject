class Mousse:
    def __init__(self, MousseID, MousseName, MousseSize, MoussePrice, MousseQuantity,
                 OrderID, OrderDate, OrderTotal, OrderStatus):
        self.MousseID = MousseID
        self.MousseName = MousseName
        self.MousseSize = MousseSize
        self.MoussePrice = MoussePrice
        self.MousseQuantity = MousseQuantity
        self.OrderID = OrderID
        self.OrderDate = OrderDate
        self.OrderTotal = OrderTotal
        self.OrderStatus = OrderStatus
    def __str__(self):
        return (f'{self.MousseID}\t{self.MousseName}\t{self.MousseSize}\t{self.MoussePrice}\t'
                f'{self.MousseQuantity}\t{self.OrderID}\t {self.OrderDate}\t{self.OrderTotal}\t'
                f'{self.OrderStatus}')