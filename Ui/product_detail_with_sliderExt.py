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
        try:
            if not self.table_widget or self.table_widget.rowCount() == 0:
                print("Table widget is empty or not available")
                self.reject()
                return
            
            if self.current_row < 0 or self.current_row >= self.table_widget.rowCount():
                print(f"Invalid row index: {self.current_row}, total rows: {self.table_widget.rowCount()}")
                self.current_row = 0  # Reset to first row if invalid
            
            # Make sure items exist at this row
            for col in range(4):  # Check first 4 columns (id, name, price, quantity)
                if not self.table_widget.item(self.current_row, col):
                    print(f"Missing item at row {self.current_row}, column {col}")
                    self.reject()
                    return

            # Get product data safely
            product_id = self.table_widget.item(self.current_row, 0).text()
            product_name = self.table_widget.item(self.current_row, 1).text()
            
            print(f"Loading details for product: {product_id} - {product_name}")
            
            # Chuyển đổi an toàn
            try:
                price_text = self.table_widget.item(self.current_row, 2).text()
                quantity_text = self.table_widget.item(self.current_row, 3).text()
                
                # Xử lý dấu phẩy trong định dạng số nếu có
                price_text = price_text.replace(',', '')
                product_price = float(price_text)
                product_quantity = int(quantity_text)
            except ValueError as e:
                print(f"Error converting price '{price_text}' or quantity '{quantity_text}': {str(e)}")
                product_price = 0
                product_quantity = 1

            # Set product details in the UI
            self.label_title.setText(product_name)
            self.label_price.setText(f"{int(product_price):,} VNĐ")

            # Find product in order_data to get description
            product = None
            if self.order_data:
                for item in self.order_data:
                    if hasattr(item, 'product_id') and item.product_id == product_id:
                        product = item
                        break

            # Set notes if they exist
            if product and hasattr(product, 'notes'):
                self.note_input.setText(product.notes)
            else:
                self.note_input.clear()

            # Set window title
            self.setWindowTitle(f"Product Details - {product_name}")
            
        except Exception as e:
            import traceback
            print(f"Error in load_product_details: {str(e)}")
            traceback.print_exc()

    def get_product_description(self, product_id):
        """Phương thức này vẫn được giữ lại nhưng có thể không được sử dụng nữa"""
        # Không cần thiết nếu không còn hiển thị description
        # Có thể giữ lại cho các tính năng trong tương lai
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

    def show_prev_product(self):
        """Show the previous product in the table"""
        try:
            if self.total_rows > 1:
                # Lưu ghi chú của sản phẩm hiện tại trước khi chuyển
                self.save_current_product_notes()
                
                # Tính toán chỉ mục trước đó một cách chính xác
                self.current_row = (self.current_row - 1) if self.current_row > 0 else (self.total_rows - 1)
                
                print(f"Switching to previous product, new row index: {self.current_row}")
                self.load_product_details()
                self.update_navigation_buttons()
        except Exception as e:
            print(f"Error in show_prev_product: {str(e)}")
            import traceback
            traceback.print_exc()

    def show_next_product(self):
        """Show the next product in the table"""
        try:
            if self.total_rows > 1:
                # Lưu ghi chú của sản phẩm hiện tại trước khi chuyển
                self.save_current_product_notes()
                
                # Tính toán chỉ mục tiếp theo một cách chính xác
                self.current_row = (self.current_row + 1) % self.total_rows
                
                print(f"Switching to next product, new row index: {self.current_row}")
                self.load_product_details()
                self.update_navigation_buttons()
        except Exception as e:
            print(f"Error in show_next_product: {str(e)}")
            import traceback
            traceback.print_exc()

    def save_current_product_notes(self):
        """Lưu ghi chú của sản phẩm hiện tại"""
        try:
            if self.total_rows > 0 and 0 <= self.current_row < self.total_rows:
                if not self.table_widget.item(self.current_row, 0):
                    return
                
                product_id = self.table_widget.item(self.current_row, 0).text()
                notes = self.note_input.toPlainText()

                # Cập nhật ghi chú trong order_data
                if self.order_data:
                    for item in self.order_data:
                        if hasattr(item, 'product_id') and item.product_id == product_id:
                            item.notes = notes
                            print(f"Saved notes for product {product_id}: {notes}")
                            break
        except Exception as e:
            print(f"Error saving notes: {str(e)}")

    def update_navigation_buttons(self):
        """Update the state of navigation buttons"""
        # Disable navigation buttons if there's only one product
        has_multiple_products = self.total_rows > 1
        self.btn_prev_image.setEnabled(has_multiple_products)
        self.btn_next_image.setEnabled(has_multiple_products)

    def accept(self):
        """Override accept to save notes before closing"""
        try:
            # Save notes to the product
            if self.total_rows > 0 and self.current_row < self.total_rows:
                if not self.table_widget.item(self.current_row, 0):
                    super().accept()
                    return
                
                product_id = self.table_widget.item(self.current_row, 0).text()
                notes = self.note_input.toPlainText()

                # Update notes in order_data
                if self.order_data:
                    for item in self.order_data:
                        if hasattr(item, 'product_id') and item.product_id == product_id:
                            item.notes = notes
                            break
        except Exception as e:
            print(f"Error in accept method: {str(e)}")
        
        super().accept()
