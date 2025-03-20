from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class InvoiceReportDialog(QDialog):
    def __init__(self, customer, order, parent=None):
        super().__init__(parent)
        self.customer = customer
        self.order = order
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Order Report")
        self.setMinimumSize(800, 600)
        
        # Main layout
        layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("CADTY - Order Report")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # Customer information
        customer_info = QLabel("Customer Information:")
        customer_info.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(customer_info)
        
        customer_details = f"""
        Customer ID: {self.customer.customer_id}
        Customer Name: {self.customer.name}
        Phone Number: {self.customer.phone}
        Address: {self.customer.address}
        """
        customer_label = QLabel(customer_details)
        customer_label.setFont(QFont("Arial", 10))
        layout.addWidget(customer_label)
        
        # Order information
        order_info = QLabel("Order Information:")
        order_info.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(order_info)
        
        order_details = f"""
        Order ID: {self.order['order_id']}
        Order Date: {self.order['order_date']}
        Payment Method: {self.order['payment_method']}
        Status: {self.order['status']}
        """
        order_label = QLabel(order_details)
        order_label.setFont(QFont("Arial", 10))
        layout.addWidget(order_label)
        
        # Order details table
        table_label = QLabel("Order Details:")
        table_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(table_label)
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Product ID", "Product Name", "Unit Price", "Quantity", "Subtotal"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)
        
        # Add data to table
        self.load_order_items()
        
        # Total amount
        total_label = QLabel(f"Total Amount: {self.order['total_amount']:,} VND")
        total_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        total_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(total_label)
        
        self.setLayout(layout)

    def load_order_items(self):
        self.table.setRowCount(len(self.order['items']))
        
        for row, item in enumerate(self.order['items']):
            # Product ID
            product_id = QTableWidgetItem(item['product_id'])
            product_id.setFlags(product_id.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 0, product_id)
            
            # Product Name
            name = QTableWidgetItem(item['name'])
            name.setFlags(name.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 1, name)
            
            # Unit Price
            price = QTableWidgetItem(f"{item['price']:,}")
            price.setFlags(price.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 2, price)
            
            # Quantity
            quantity = QTableWidgetItem(str(item['quantity']))
            quantity.setFlags(quantity.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 3, quantity)
            
            # Subtotal
            subtotal = QTableWidgetItem(f"{item['subtotal']:,}")
            subtotal.setFlags(subtotal.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 4, subtotal) 