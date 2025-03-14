from PyQt6.QtWidgets import QDialog
from Ui.product_detail_with_slider import Ui_ProductDetailDialog


class ProductDetailDialog(QDialog, Ui_ProductDetailDialog):
    def __init__(self, parent=None, table_widget=None, current_row=0, order_data=None):
        super().__init__(parent)
        self.setupUi(self)
        self.table_widget = table_widget
        self.current_row = current_row
        self.total_rows = table_widget.rowCount()
        self.order_data = order_data

        # Load the current product details
        self.load_product_details()

        # Connect buttons
        self.btn_back_to_cart.clicked.connect(self.accept)
        self.btn_prev_image.clicked.connect(self.show_prev_product)
        self.btn_next_image.clicked.connect(self.show_next_product)

        # Update button text to reflect they navigate between products
        self.btn_prev_image.setText("< Prev Product")
        self.btn_next_image.setText("Next Product >")

        # Update navigation button states
        self.update_navigation_buttons()

    def load_product_details(self):
        """Load the details of the current product"""
        if self.total_rows == 0 or self.current_row >= self.total_rows:
            self.reject()  # Close dialog if no valid row
            return

        # Get product data from the selected row
        product_id = self.table_widget.item(self.current_row, 0).text()
        product_name = self.table_widget.item(self.current_row, 1).text()
        product_price = float(self.table_widget.item(self.current_row, 2).text())
        product_quantity = int(self.table_widget.item(self.current_row, 3).text())

        # Set product details in the UI
        self.label_title.setText(product_name)
        self.label_price.setText(f"{int(product_price):,} VNĐ")

        # Find product in order_data to get description
        product = None
        for item in self.order_data:
            if item.product_id == product_id:
                product = item
                break

        # Set description and notes
        if product and hasattr(product, 'description') and product.description:
            self.label_description.setText(product.description)
        else:
            self.label_description.setText(self.get_product_description(product_id))

        # Set notes if they exist
        if product and hasattr(product, 'notes'):
            self.note_input.setText(product.notes)

        # Load product image
        self.load_product_image(product_id, product)

        # Set window title
        self.setWindowTitle(f"Product Details - {product_name}")

    def get_product_description(self, product_id):
        """Get the description for a product"""
        # This would ideally come from a database
        descriptions = {
            "CB1": "Romance Blossom - A delicate mousse cake with layers of rose-infused cream and raspberry compote.",
            "CB2": "Royal Nut Harmony - A luxurious blend of premium nuts and caramel on a buttery base.",
            "CB3": "Berry Symphony - A harmonious blend of mixed berries on a light sponge base.",
            "CB4": "Pandora Delight - A rich chocolate mousse with hazelnut crunch.",
            "CB5": "Amber Kiss - A caramel-infused mousse with a hint of sea salt.",
            "CB6": "Imperial Oolong - An elegant tea-infused mousse with white chocolate accents.",
            "CB7": "Crimson Melody - A vibrant red velvet tart with cream cheese filling.",
            "CB8": "Banana Cloud - A light banana cream tart with caramelized banana slices.",
            "CB9": "Very Merry - A festive mixed berry tart with vanilla custard.",
            "CB10": "Cheese Crust - A savory-sweet cheese tart with a buttery crust.",
            # Add more descriptions as needed
        }
        return descriptions.get(product_id, "No description available for this product.")

    def load_product_image(self, product_id, product=None):
        """Load the image for a product"""
        # Try to load image from product object first
        if product and hasattr(product, 'image_path') and product.image_path:
            try:
                pixmap = QPixmap(product.image_path)
                self.label_image.setPixmap(pixmap)
                self.label_image.setScaledContents(True)
                return
            except:
                pass  # Fall back to default handling

        # Default image handling
        image_path = f"images/{product_id}.jpg"
        try:
            pixmap = QPixmap(image_path)
            self.label_image.setPixmap(pixmap)
            self.label_image.setScaledContents(True)
        except:
            self.label_image.setText(f"Image for {product_id}")
            self.label_image.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 8px;")

    def show_prev_product(self):
        """Show the previous product in the table"""
        if self.total_rows > 1:
            self.current_row = (self.current_row - 1) % self.total_rows
            self.load_product_details()
            self.update_navigation_buttons()

    def show_next_product(self):
        """Show the next product in the table"""
        if self.total_rows > 1:
            self.current_row = (self.current_row + 1) % self.total_rows
            self.load_product_details()
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        """Update the state of navigation buttons"""
        # Disable navigation buttons if there's only one product
        has_multiple_products = self.total_rows > 1
        self.btn_prev_image.setEnabled(has_multiple_products)
        self.btn_next_image.setEnabled(has_multiple_products)

    def accept(self):
        """Override accept to save notes before closing"""
        # Save notes to the product
        if self.total_rows > 0:
            product_id = self.table_widget.item(self.current_row, 0).text()
            notes = self.note_input.toPlainText()

            # Update notes in order_data
            for item in self.order_data:
                if item.product_id == product_id:
                    item.notes = notes
                    break

        super().accept()
