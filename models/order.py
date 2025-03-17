from datetime import datetime

class Order:
    def __init__(self, order_id=None, customer_id=None, order_date=None,
                 total_amount=0, payment_method=None, status="pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date or datetime.now().isoformat()
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.status = status
        self.items = []  # Danh sách chi tiết đơn hàng