from PyQt6.QtWidgets import QTableWidgetItem

from self_order import Ui_MainWindow


class SelfOrderExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.order_count = 0
        self.total_amount = 0.0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.pushButton_Mousse.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Mousse))   #ấn vào cái nào thì hiện menu cái đó
        self.pushButton_Tart.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Tart))
        self.pushButton_Croissant.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Croissant))
        self.pushButton_Cookies.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Cookies))
        self.pushButton_Drinks.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Drinks))

        self.pushButton_add_matcha.clicked.connect(self.addMatchaToOrder)
    def showWindow(self):
        self.MainWindow.show()

    def setupTableHeaders(self):
        self.tableWidget_order.setColumnCount(5)
        headers = ["Item", "Price", 'Size', "Quantity", "Subtotal"]
        self.tableWidget_order.setHorizontalHeaderLabels(headers)
    def addMatchaToOrder(self):
        item_name = "Matcha S'more"
        item_price = 70000
        item_size = "Regular"
        item_quantity = 1
        item_subtotal = item_price * item_quantity
        self.total_amount += item_subtotal
        row_position = self.tableWidget_order.rowCount()  #add new row to table
        self.tableWidget_order.insertRow(row_position)
        self.tableWidget_order.setItem(row_position, 0, QTableWidgetItem(item_name))
        self.tableWidget_order.setItem(row_position, 1, QTableWidgetItem(f"{item_price}"))
        self.tableWidget_order.setItem(row_position, 2, QTableWidgetItem(str(item_size)))
        self.tableWidget_order.setItem(row_position, 3, QTableWidgetItem(item_quantity))
        self.tableWidget_order.setItem(row_position, 4, QTableWidgetItem(f"{item_subtotal}"))

        self.order_count += 1
        self.tableWidget_order.resizeColumnsToContents()