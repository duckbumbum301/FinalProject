class Product:
    def __init__(self, product_id=None, name=None, price=0, quantity=0, notes=None,
                 customer_name=None, customer_phone=None, customer_email=None,
                 customer_address=None, payment_method=None, discount=None, category=None,
                 description=None, image_path=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.notes = notes
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_email = customer_email
        self.customer_address = customer_address
        self.payment_method = payment_method
        self.discount = discount
        self.category = category
        self.description = description
        self.image_path = image_path

class Mousse(Product):
    def __init__(self, product_id=None, name=None, price=0, quantity=0, notes=None, **kwargs):
        super().__init__(product_id, name, price, quantity, notes, **kwargs)
        self.category = "Mousse"
        self.description = ""
        self.image_path = ""

class Tart(Product):
    def __init__(self, product_id=None, name=None, price=0, quantity=0, notes=None, **kwargs):
        super().__init__(product_id, name, price, quantity, notes, **kwargs)
        self.category = "Tart"
        self.description = ""
        self.image_path = ""

class Croissant(Product):
    def __init__(self, product_id=None, name=None, price=0, quantity=0, notes=None, **kwargs):
        super().__init__(product_id, name, price, quantity, notes, **kwargs)
        self.category = "Croissant"
        self.description = ""
        self.image_path = ""

class Cookies(Product):
    def __init__(self, product_id=None, name=None, price=0, quantity=0, notes=None, **kwargs):
        super().__init__(product_id, name, price, quantity, notes, **kwargs)
        self.category = "Cookies"
        self.description = ""
        self.image_path = ""

class Drinks(Product):
    def __init__(self, product_id=None, name=None, price=0, quantity=0, notes=None, **kwargs):
        super().__init__(product_id, name, price, quantity, notes, **kwargs)
        self.category = "Drinks"
        self.description = ""
        self.image_path = ""