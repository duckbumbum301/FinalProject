from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog
from Ui.product_detail_with_slider import Ui_ProductDetailDialog
import os
from PyQt6.QtCore import Qt


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

        # Default image handling from full_images directory
        try:
            # Xác định đường dẫn hình ảnh dựa trên product_id
            if product_id == 'CB1':
                image_path = "../full_images/CB1.jpg"
            elif product_id == 'CB2':
                image_path = "../full_images/CB2.jpg"
            elif product_id == 'CB3':
                image_path = "../full_images/CB3.jpg"
            elif product_id == 'CB4':
                image_path = "full_images/CB4.jpg"
            elif product_id == 'CB5':
                image_path = "full_images/CB5.jpg"
            elif product_id == 'CB6':
                image_path = "full_images/CB6.jpg"
            elif product_id == 'CB7':
                image_path = "full_images/CB7.jpg"
            elif product_id == 'CB8':
                image_path = "full_images/CB8.jpg"
            elif product_id == 'CB9':
                image_path = "full_images/CB9.jpg"
            elif product_id == 'CB10':
                image_path = "full_images/CB10.jpg"
            elif product_id == 'CB11':
                image_path = "full_images/CB11.jpg"
            elif product_id == 'CB12':
                image_path = "full_images/CB12.jpg"
            elif product_id == 'CB13':
                image_path = "full_images/CB13.png"
            elif product_id == 'CB14':
                image_path = "full_images/CB14.png"
            elif product_id == 'CB15':
                image_path = "full_images/CB15.png"
            elif product_id == 'CB16':
                image_path = "full_images/CB16.png"
            elif product_id == 'CB17':
                image_path = "full_images/CB17.png"
            elif product_id == 'CB18':
                image_path = "full_images/CB18.png"
            elif product_id == 'CB19':
                image_path = "full_images/CB19.jpg"
            elif product_id == 'CB20':
                image_path = "full_images/CB20.jpg"
            elif product_id == 'CB21':
                image_path = "full_images/CB21.jpg"
            elif product_id == 'CB22':
                image_path = "full_images/CB22.jpg"
            elif product_id == 'CB23':
                image_path = "full_images/CB23.jpg"
            elif product_id == 'CB24':
                image_path = "full_images/CB24.jpg"
            elif product_id == 'CB25':
                image_path = "full_images/CB25.png"
            elif product_id == 'CB26':
                image_path = "full_images/CB26.png"
            elif product_id == 'CB27':
                image_path = "full_images/CB27.png"
            elif product_id == 'CB28':
                image_path = "full_images/CB28.jpg"
            elif product_id == 'CB29':
                image_path = "full_images/CB29.jpg"
            else:
                # Nếu không tìm thấy product_id phù hợp
                self.label_image.setText(f"Không có hình ảnh cho {product_id}")
                self.label_image.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 8px;")
                return
            
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    # Tính toán kích thước để giữ tỷ lệ khung hình
                    label_size = self.label_image.size()
                    scaled_pixmap = pixmap.scaled(
                        label_size, 
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    self.label_image.setPixmap(scaled_pixmap)
                    self.label_image.setScaledContents(False)  # Tắt scaled contents để giữ tỷ lệ
                    return
                
            # Nếu không tìm thấy hình ảnh hoặc không thể load
            self.label_image.setText(f"Không có hình ảnh cho {product_id}")
            self.label_image.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 8px;")
            
        except Exception as e:
            print(f"Lỗi khi tải hình ảnh cho {product_id}: {str(e)}")
            self.label_image.setText(f"Không thể tải hình ảnh cho {product_id}")
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
