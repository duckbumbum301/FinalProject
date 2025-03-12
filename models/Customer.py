class Customer:
    def __init__(self, CusID, CusName, CusAddress, CusPhone, Payment,
                 OrderID, OrderDate, OrderTotal, OrderStatus,
                 ProductID, ProductName, ProductSize, ProductPrice, ProductQuantity,
                 OrderDetailID):
        self.CusID = CusID
        self.CusName = CusName
        self.CusAddress = CusAddress
        self.CusPhone = CusPhone
        self.Payment = Payment
        self.OrderID = OrderID
        self.OrderDate = OrderDate
        self.OrderTotal = OrderTotal
        self.OrderStatus = OrderStatus
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.ProductSize = ProductSize
        self.ProductPrice = ProductPrice
        self.ProductQuantity = ProductQuantity
        self.OrderDetailID = OrderDetailID
    def __str__(self):
        return (f'{self.CusID}\t{self.CusName}\t{self.CusAddress}\t{self.CusPhone}\t'
                f'{self.Payment}\t{self.OrderID}\t {self.OrderDate}\t{self.OrderTotal}\t'
                f'{self.OrderStatus}\t{self.ProductID}\t{self.ProductName}\t{self.ProductSize}\t'
                f'{self.ProductPrice}\t{self.ProductQuantity}\t{self.OrderDetailID}')