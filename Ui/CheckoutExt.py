from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Ui.Checkout import Ui_CheckoutWindow
from libs.JsonFileFactory import JsonFileFactory
from models.Product import Product


class CheckoutExt(QMainWindow, Ui_CheckoutWindow):
    def __init__(self, order_data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.order_data = order_data
        self.json_factory = JsonFileFactory()

        # Set up the order summary
        self.display_order_summary()

        # Connect buttons
        self.pushButtonDone.clicked.connect(self.process_order)
        self.pushButton_Back.clicked.connect(self.close)

        # Set default payment method
        self.radioButton_cash.setChecked(True)

    def display_order_summary(self):
        """Display the order summary in the text edit"""
        summary = "=== ORDER SUMMARY ===\n\n"
        total = 0

        for item in self.order_data:
            product_id = item.product_id
            name = item.name
            price = item.price
            quantity = item.quantity
            subtotal = price * quantity
            total += subtotal

            summary += f"{product_id} - {name}\n"
            summary += f"Price: {price:,} VNĐ x {quantity} = {subtotal:,} VNĐ\n"
            if hasattr(item, 'notes') and item.notes:
                summary += f"Notes: {item.notes}\n"
            summary += "\n"

        summary += f"Total: {total:,} VNĐ"

        # Set the summary text and total
        self.order_summary_content.setText(summary)
        self.lineEditTotal.setText(f"{total:,} VNĐ")
        self.lineEditTotal.setReadOnly(True)

    def process_order(self):
        """Process the order when Done button is clicked"""
        # Get customer details
        customer_name = self.lineEditName.text()
        customer_phone = self.lineEditPhone.text()
        customer_email = self.lineEditEmail.text()
        customer_address = self.lineEditAddress.text()

        # Validate required fields
        if not customer_name or not customer_phone:
            QMessageBox.warning(self, "Missing Information", "Please provide at least customer name and phone number.")
            return

        # Get payment method
        payment_method = "Cash" if self.radioButton_cash.isChecked() else "Online"

        try:
            # Step 1: Load existing products from JSON
            products = self.json_factory.read_data("../data/orders.json", Product)

            # Step 2: Add new order products to the list
            for item in self.order_data:
                # Add customer info and payment method as attributes
                item.customer_name = customer_name
                item.customer_phone = customer_phone
                item.customer_email = customer_email
                item.customer_address = customer_address
                item.payment_method = payment_method
                item.discount = self.lineEditDiscount.text()

                # Append to products list
                products.append(item)

            # Step 3: Save updated products list to JSON
            self.json_factory.write_data(products, "../data/orders.json")

            QMessageBox.information(self, "Success", "Order has been processed successfully!")
            self.close()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save order: {str(e)}")