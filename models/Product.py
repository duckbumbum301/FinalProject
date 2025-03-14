
class Product:
    def __init__(self, product_id, name, price,quantity, description="", image_path=""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.image_path = image_path
        self.quantity=quantity

    def __str__(self):
        return f"{self.name}\t{self.price}\t{self.quantity}\t{self.description}\t{self.image_path}"


class Mousse(Product):
    def __init__(self, product_id, name, price,quantity, description="", image_path=""):
        super().__init__(product_id, name, price,quantity, description, image_path)
        self.category = "Mousse"

class Tart(Product):
    def __init__(self, product_id, name, price,quantity, description="", image_path=""):
        super().__init__(product_id, name, price,quantity, description, image_path)
        self.category = "Tart"

class Croissant(Product):
    def __init__(self, product_id, name, price,quantity, description="", image_path=""):
        super().__init__(product_id, name, price,quantity, description, image_path)
        self.category = "Croissant"

class Cookies(Product):
    def __init__(self, product_id, name, price,quantity, description="", image_path=""):
        super().__init__(product_id, name, price,quantity, description, image_path)
        self.category = "Cookies"

class Drinks(Product):
    def __init__(self, product_id, name, price,quantity, description="", image_path=""):
        super().__init__(product_id, name, price,quantity, description, image_path)
        self.category = "Drinks"
