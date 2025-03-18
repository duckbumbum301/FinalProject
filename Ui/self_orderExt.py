from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView, QMessageBox, QDialog

from Ui.CheckoutExt import CheckoutExt
from Ui.product_detail_with_sliderExt import ProductDetailDialog
from Ui.self_order import Ui_MainWindow
from libs.JsonFileFactory import JsonFileFactory
from models.product import Croissant, Tart, Mousse, Cookies, Drinks, Product


class SelfOrderExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.order_count = 0
        self.total_amount = 0.0
        self.order_data = []
        self.json_factory = JsonFileFactory()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupTableHeaders()
        self.setupSignalsAndSlots()
        # Khởi tạo hiển thị tổng tiền
        if hasattr(self, "lineEdit_total"):
            self.lineEdit_total.setText("0 VNĐ")
            # Không cho phép chỉnh sửa trực tiếp
            self.lineEdit_total.setReadOnly(True)

        self.tableWidget_order.cellDoubleClicked.connect(self.showProductDetail)
        self.pushButtonProceed.clicked.connect(self.openCheckout)
    def setupSignalsAndSlots(self):
        # Menu navigation
        self.pushButton_Mousse.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Mousse))   #ấn vào cái nào thì hiện menu cái đó
        self.pushButton_Tart.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Tart))
        self.pushButton_Croissant.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Croissant))
        self.pushButton_Cookies.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Cookies))
        self.pushButton_Drinks.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Drinks))
        
        # Product buttons
        self.pushButton_add1.clicked.connect(self.addRomanceToOrder)
        self.pushButton_add2.clicked.connect(self.addRoyalToOrder)
        self.pushButton_add3.clicked.connect(self.addBerryToOrder)
        self.pushButton_add4.clicked.connect(self.addPandoraToOrder)
        self.pushButton_add5.clicked.connect(self.addAmberToOrder)
        self.pushButton_add6.clicked.connect(self.addImperialToOrder)
        self.pushButton_add7.clicked.connect(self.addCrimsonToOrder)
        self.pushButton_add8.clicked.connect(self.addBananaToOrder)
        self.pushButton_add9.clicked.connect(self.addVeryToOrder)
        self.pushButton_add10.clicked.connect(self.addCheeseToOrder)
        self.pushButton_add11.clicked.connect(self.addPinkToOrder)
        self.pushButton_add12.clicked.connect(self.addSunnyToOrder)
        self.pushButton_add13.clicked.connect(self.addHoneyToOrder)
        self.pushButton_add14.clicked.connect(self.addStrawberryToOrder)
        self.pushButton_add15.clicked.connect(self.addClassicToOrder)
        self.pushButton_add16.clicked.connect(self.addBlushToOrder)
        self.pushButton_add17.clicked.connect(self.addTiramisiuToOrder)
        self.pushButton_add18.clicked.connect(self.addEarlgreyToOrder)
        self.pushButton_add19.clicked.connect(self.addChocoChipToOrder)
        self.pushButton_add20.clicked.connect(self.addDarkToOrder)
        self.pushButton_add21.clicked.connect(self.addCookiesCreamToOrder)
        self.pushButton_add22.clicked.connect(self.addCreamyMatchaToOrder)
        self.pushButton_add23.clicked.connect(self.addTwistedToOrder)
        self.pushButton_add24.clicked.connect(self.addOreoToOrder)
        self.pushButton_add25.clicked.connect(self.addTiraMissUToOrder)
        self.pushButton_add26.clicked.connect(self.addMatchaToOrder)
        self.pushButton_add27.clicked.connect(self.addChocoSmoreToOrder)
        self.pushButton_add28.clicked.connect(self.addLushToOrder)
        self.pushButton_add29.clicked.connect(self.addBergamotToOrder)


        self.pushButtonDelete.clicked.connect(self.removeSelectedItem)
        self.pushButtonNewOrder.clicked.connect(self.clearCart)
        self.pushButtonEdit.clicked.connect(self.enableOrderEditing)

    def showWindow(self):
        self.MainWindow.show()

    def showProductDetail(self, row, column):
        if self.tableWidget_order.rowCount() == 0:
            return

            # Create and show the product detail dialog
        dialog = ProductDetailDialog(
            parent=self.MainWindow,
            table_widget=self.tableWidget_order,
            current_row=row,
            order_data = self.order_data
        )

        result = dialog.exec()

        # If the dialog was accepted (user clicked "Back to Cart +"), you could
        # potentially update the quantity or add notes to the order here
        if result == QDialog.DialogCode.Accepted:
            notes = dialog.note_input.toPlainText()
            if notes:
                product_name = self.tableWidget_order.item(row, 1).text()
                print(f"Notes for {product_name}: {notes}")

    def setupTableHeaders(self):
        self.tableWidget_order.setColumnCount(5)
        headers = ["Product ID", "Product Name", "Price", "Quantity", "Subtotal"]
        self.tableWidget_order.setHorizontalHeaderLabels(headers)

        header_view = self.tableWidget_order.horizontalHeader()
        header_view.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_order.setRowCount(0)
        self.disableOrderEditing()
        
    def addProductToOrder(self, product_id, product_name, product_price, product_quantity=1):
        for row in range(self.tableWidget_order.rowCount()):
            id_item = self.tableWidget_order.item(row, 0)
            if id_item and id_item.text() == product_id:
                # Sản phẩm đã tồn tại, tăng số lượng
                quantity_item = self.tableWidget_order.item(row, 3)
                current_quantity = int(quantity_item.text())
                new_quantity = current_quantity + 1
                quantity_item.setText(str(new_quantity))
                
                # Cập nhật thành tiền
                new_subtotal = product_price * new_quantity
                self.tableWidget_order.item(row, 4).setText(str(new_subtotal))
                
                # Cập nhật tổng tiền
                self.total_amount += product_price
                self.updateTotalAmountDisplay()

                for item in self.order_data:
                    if item.product_id == product_id:
                        item.quantity = new_quantity
                        break

                # Đảm bảo cột số lượng không thể chỉnh sửa trực tiếp
                self.disableOrderEditing()
                return
        
        # Nếu sản phẩm chưa có trong giỏ hàng, thêm mới
        product_subtotal = product_price * product_quantity

        # Cập nhật tổng tiền và đếm số lượng đơn hàng
        self.total_amount += product_subtotal
        self.order_count += 1

        # Thêm một dòng mới ở cuối bảng
        row_position = self.tableWidget_order.rowCount()
        self.tableWidget_order.insertRow(row_position)
        
        # Ghi dữ liệu vào dòng mới
        self.tableWidget_order.setItem(row_position, 0, QTableWidgetItem(product_id))
        self.tableWidget_order.setItem(row_position, 1, QTableWidgetItem(product_name))
        self.tableWidget_order.setItem(row_position, 2, QTableWidgetItem(str(product_price)))
        self.tableWidget_order.setItem(row_position, 3, QTableWidgetItem(str(product_quantity)))
        self.tableWidget_order.setItem(row_position, 4, QTableWidgetItem(str(product_subtotal)))

        # Điều chỉnh kích thước cột cho vừa nội dung
        self.tableWidget_order.resizeColumnsToContents()
        
        # Cập nhật hiển thị tổng tiền
        self.updateTotalAmountDisplay()
        
        # Đảm bảo tất cả các ô trong bảng đều không thể chỉnh sửa
        self.disableOrderEditing()

        category = self.determine_product_category(product_id)

        # Create appropriate Product subclass based on category
        if category == "Mousse":
            product = Mousse(product_id, product_name, product_price, product_quantity)
        elif category == "Tart":
            product = Tart(product_id, product_name, product_price, product_quantity)
        elif category == "Croissant":
            product = Croissant(product_id, product_name, product_price, product_quantity)
        elif category == "Cookies":
            product = Cookies(product_id, product_name, product_price, product_quantity)
        elif category == "Drinks":
            product = Drinks(product_id, product_name, product_price, product_quantity)
        else:
            product = Product(product_id, product_name, product_price, product_quantity)

        # Add description and image path if available
        product.description = self.get_product_description(product_id)
        product.image_path = f"images/{product_id}.jpg"
        product.notes = ""

        # Add to order_data
        self.order_data.append(product)

    def determine_product_category(self, product_id):
        """Determine product category based on product_id"""
        # This is a simple implementation based on product_id patterns
        # You might want to use a more robust method in a real application
        if product_id in ["CB1", "CB2", "CB3", "CB4", "CB5", "CB6"]:
            return "Mousse"
        elif product_id in ["CB7", "CB8", "CB9", "CB10"]:
            return "Tart"
        elif product_id in ["CB11", "CB12", "CB13", "CB14", "CB15", "CB16"]:
            return "Croissant"
        elif product_id in ["CB17", "CB18", "CB19", "CB20", "CB21", "CB22", "CB23", "CB24"]:
            return "Cookies"
        elif product_id in ["CB25", "CB26", "CB27", "CB28", "CB29"]:
            return "Drinks"
        else:
            return "Unknown"

    def get_product_description(self, product_id):
        """Get description for a product"""
        descriptions = {
            "CB1": "Romance Blossom - A delicate mousse cake with layers of rose-infused cream and raspberry compote.",
            "CB2": "Royal Nut Harmony - A luxurious blend of premium nuts and caramel on a buttery base.",
            # Add more descriptions as needed
        }
        return descriptions.get(product_id, "")

    def openCheckout(self):
        """Open the checkout window"""
        if self.tableWidget_order.rowCount() == 0:
            QMessageBox.information(self.MainWindow, "Empty Cart",
                                    "Your cart is empty. Please add items before proceeding to checkout.")
            return

        # Đảm bảo tính toán tổng tiền chính xác
        self.calculateTotalFromTable()
        
        try:
            # Nếu cửa sổ checkout đã tồn tại, cập nhật dữ liệu và hiển thị lại
            if hasattr(self, 'checkout_window'):
                self.checkout_window.order_data = self.order_data
                self.checkout_window.display_order_summary()
                self.checkout_window.show()
            else:
                # Tạo cửa sổ checkout mới nếu chưa tồn tại
                self.checkout_window = CheckoutExt(self.order_data, self.MainWindow)
                # Kết nối tín hiệu orderProcessed với việc làm mới giỏ hàng
                self.checkout_window.orderProcessed.connect(self.reset_cart)
                self.checkout_window.show()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể mở cửa sổ thanh toán: {str(e)}")
            # In ra log để gỡ lỗi
            print(f"Error opening checkout: {str(e)}")

    def checkoutOrder(self):
        """Modified to open checkout window instead of showing message box"""
        if self.tableWidget_order.rowCount() == 0:
            QMessageBox.information(self.MainWindow, "Thông báo", "Giỏ hàng trống!")
            return

        # Ensure total is accurate
        self.calculateTotalFromTable()

        # Open checkout window
        self.openCheckout()

    def updateTotalAmountDisplay(self):
        """Cập nhật hiển thị tổng tiền vào lineEdit_total"""
        if hasattr(self, "lineEdit_total"):
            self.lineEdit_total.setText(f"{self.total_amount:,} VNĐ")
        print(f"Tổng tiền: {self.total_amount:,} VNĐ")

    def calculateTotalFromTable(self):
        """Tính tổng tiền từ tất cả các dòng trong bảng"""
        total = 0
        for row in range(self.tableWidget_order.rowCount()):
            subtotal_item = self.tableWidget_order.item(row, 4)
            if subtotal_item:
                subtotal = float(subtotal_item.text())
                total += subtotal
                
        self.total_amount = total
        self.updateTotalAmountDisplay()
        
    def removeSelectedItem(self):
        """Xóa sản phẩm được chọn khỏi giỏ hàng"""
        selected_items = self.tableWidget_order.selectedItems()
        if not selected_items:
            QMessageBox.information(self.MainWindow, "Thông báo", "Vui lòng chọn sản phẩm cần xóa!")
            return
            
        # Lấy dòng được chọn
        selected_row = selected_items[0].row()
        
        # Lấy thông tin sản phẩm để trừ khỏi tổng tiền
        subtotal_item = self.tableWidget_order.item(selected_row, 4)
        product_id = self.tableWidget_order.item(selected_row, 0).text()

        if subtotal_item:
            subtotal = float(subtotal_item.text())
            self.total_amount -= subtotal
            
        # Xóa dòng
        self.tableWidget_order.removeRow(selected_row)
        self.order_count -= 1

        self.order_data = [item for item in self.order_data if item.product_id != product_id]

        # Cập nhật hiển thị tổng tiền
        self.updateTotalAmountDisplay()

    def enableOrderEditing(self):
        """
        Cho phép chỉnh sửa số lượng trong bảng khi bấm nút Edit
        Chỉ cho phép chỉnh sửa cột số lượng (Quantity - cột 3), các cột khác vẫn không thể chỉnh sửa
        """
        # Trước tiên, đảm bảo tất cả các ô đều không thể chỉnh sửa
        self.disableOrderEditing()
        
        # Chỉ bật khả năng chỉnh sửa cho cột số lượng (Quantity)
        for row in range(self.tableWidget_order.rowCount()):
            quantity_item = self.tableWidget_order.item(row, 3)
            if quantity_item:
                quantity_item.setFlags(quantity_item.flags() | Qt.ItemFlag.ItemIsEditable)
        
        # Kết nối sự kiện thay đổi cell để cập nhật subtotal khi số lượng thay đổi
        try:
            self.tableWidget_order.cellChanged.disconnect()
        except:
            pass
        self.tableWidget_order.cellChanged.connect(self.updateSubtotalOnEdit)
        
        QMessageBox.information(self.MainWindow, "Chế độ chỉnh sửa", 
                               "Đã bật chế độ chỉnh sửa số lượng. Hãy nhấp vào ô số lượng và nhập giá trị mới.")
        
    def disableOrderEditing(self):
        """
        Vô hiệu hóa khả năng chỉnh sửa tất cả các ô trong bảng
        """
        # Ngắt kết nối sự kiện cellChanged để tránh kích hoạt khi thiết lập lại flags
        try:
            self.tableWidget_order.cellChanged.disconnect()
        except:
            pass
        
        # Vô hiệu hóa khả năng chỉnh sửa cho tất cả các ô
        for row in range(self.tableWidget_order.rowCount()):
            for col in range(self.tableWidget_order.columnCount()):
                item = self.tableWidget_order.item(row, col)
                if item:
                    # Loại bỏ flag ItemIsEditable nhưng giữ các flags khác
                    current_flags = item.flags()
                    new_flags = current_flags & ~Qt.ItemFlag.ItemIsEditable
                    item.setFlags(new_flags)

    def updateSubtotalOnEdit(self, row, column):
        """Cập nhật thành tiền khi số lượng thay đổi"""
        if column == 3:  # Cột số lượng
            try:
                quantity_item = self.tableWidget_order.item(row, 3)
                price_item = self.tableWidget_order.item(row, 2)
                subtotal_item = self.tableWidget_order.item(row, 4)
                
                if quantity_item and price_item and subtotal_item:
                    quantity = int(quantity_item.text())
                    price = float(price_item.text())
                    
                    if quantity <= 0:
                        QMessageBox.warning(self.MainWindow, "Cảnh báo", "Số lượng phải lớn hơn 0!")
                        quantity = 1
                        quantity_item.setText("1")
                    
                    # Lấy subtotal cũ để trừ khỏi tổng
                    old_subtotal = float(subtotal_item.text())
                    
                    # Tính subtotal mới
                    new_subtotal = price * quantity
                    subtotal_item.setText(str(new_subtotal))
                    
                    # Cập nhật tổng tiền
                    self.total_amount = self.total_amount - old_subtotal + new_subtotal
                    self.updateTotalAmountDisplay()
            except ValueError:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập số lượng hợp lệ!")
                quantity_item.setText("1")  # Reset về 1 nếu có lỗi
                self.updateSubtotalOnEdit(row, column)  # Gọi lại để cập nhật

    def clearCart(self):
        self.tableWidget_order.setRowCount(0)
        self.total_amount = 0
        self.order_count = 0
        self.updateTotalAmountDisplay()

        # Clear order_data
        self.order_data = []

    def reset_cart(self):
        """Reset giỏ hàng và làm mới giao diện sau khi đơn hàng được xử lý thành công"""
        # Xóa tất cả dữ liệu trong bảng
        self.tableWidget_order.setRowCount(0)
        
        # Reset các biến theo dõi
        self.total_amount = 0
        self.order_count = 0
        self.order_data = []
        
        # Cập nhật hiển thị tổng tiền
        self.updateTotalAmountDisplay()
        
        # Đảm bảo các nút và trạng thái được reset
        self.disableOrderEditing()
        
        print("Giỏ hàng đã được làm mới")

    def addMatchaToOrder(self):
        self.addProductToOrder("CB26", "Matcha S'more", 70000)

    def addRomanceToOrder(self):
        self.addProductToOrder("CB1", "Romance Blossom", 480000)

    def addRoyalToOrder(self):
        self.addProductToOrder("CB2", "Royal Nut Harmony", 480000)

    def addBerryToOrder(self):
        self.addProductToOrder("CB3", "Berry Symphony", 480000)

    def addPandoraToOrder(self):
        self.addProductToOrder("CB4", "Pandora Delight", 480000)

    def addAmberToOrder(self):
        self.addProductToOrder("CB5", "Amber Kiss", 480000)

    def addImperialToOrder(self):
        self.addProductToOrder("CB6", "Imperial Oolong", 480000)
        
    def addCrimsonToOrder(self):
        self.addProductToOrder("CB7", "Crimson Melody", 55000)
        
    def addBananaToOrder(self):
        self.addProductToOrder("CB8", "Banana Cloud", 60000)
        
    def addVeryToOrder(self):
        self.addProductToOrder("CB9", "Very Merry", 60000)
        
    def addCheeseToOrder(self):
        self.addProductToOrder("CB10", "Cheese Crust", 65000)
        
    def addPinkToOrder(self):
        self.addProductToOrder("CB11", "Pink Velvet", 120000)
        
    def addSunnyToOrder(self):
        self.addProductToOrder("CB12", "Sunny Kernel", 110000)
        
    def addHoneyToOrder(self):
        self.addProductToOrder("CB13", "Honey Glaze", 65000)
        
    def addStrawberryToOrder(self):
        self.addProductToOrder("CB14", "Strawberry Breeze", 60000)
        
    def addClassicToOrder(self):
        self.addProductToOrder("CB15", "Classic", 50000)
        
    def addBlushToOrder(self):
        self.addProductToOrder("CB16", "Blush Crust", 100000)
        
    def addTiramisiuToOrder(self):
        self.addProductToOrder("CB17", "Tiramisiu Cake", 100000)
        
    def addEarlgreyToOrder(self):
        self.addProductToOrder("CB18", "Earl-Grey & Almond", 100000)
        
    def addChocoChipToOrder(self):
        self.addProductToOrder("CB19", "Classic Choco Chip", 35000)
        
    def addDarkToOrder(self):
        self.addProductToOrder("CB20", "Dark Mix", 40000)
        
    def addCookiesCreamToOrder(self):
        self.addProductToOrder("CB21", "Cookies&Cream", 45000)
        
    def addCreamyMatchaToOrder(self):
        self.addProductToOrder("CB22", "Creamy Matcha", 45000)
        
    def addTwistedToOrder(self):
        self.addProductToOrder("CB23", "Twisted Love", 45000)
        
    def addOreoToOrder(self):
        self.addProductToOrder("CB24", "Oreo Chocolate", 45000)
        
    def addTiraMissUToOrder(self):
        self.addProductToOrder("CB25", "Tira-Miss-U", 55000)
        
    def addChocoSmoreToOrder(self):
        self.addProductToOrder("CB27", "Choco S'more", 65000)
        
    def addLushToOrder(self):
        self.addProductToOrder("CB28", "Lush Pear", 60000)
        
    def addBergamotToOrder(self):
        self.addProductToOrder("CB29", "Bergamot Brew", 60000)