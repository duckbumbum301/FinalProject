class Croissant:
    def __init__(self, CroissantID, CroissantName, CroissantSize, CroissantPrice, CroissantQuantity,
                 OrderID, OrderDate, OrderTotal, OrderStatus):
        self.CroissantID = CroissantID
        self.CroissantName = CroissantName
        self.CroissantSize = CroissantSize
        self.CroissantPrice = CroissantPrice
        self.CroissantQuantity = CroissantQuantity
        self.OrderID = OrderID
        self.OrderDate = OrderDate
        self.OrderTotal = OrderTotal
        self.OrderStatus = OrderStatus
    def __str__(self):
        return (f'{self.CroissantID}\t{self.CroissantName}\t{self.CroissantSize}\t{self.CroissantPrice}\t'
                f'{self.CroissantQuantity}\t{self.OrderID}\t{self.OrderDate}\t{self.OrderTotal}\t{self.OrderStatus}')