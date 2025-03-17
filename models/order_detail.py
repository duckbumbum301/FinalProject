class OrderDetail:
    def __init__(self, order_id=None, product_id=None, name=None, price=0,
                 quantity=0, notes=None):
        self.order_id = order_id
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.notes = notes
        self.subtotal = price * quantity