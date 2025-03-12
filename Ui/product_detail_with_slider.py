# Form implementation generated from reading ui file 'D:\FINAL_KTLT\Ui_Cadty\Ui\product_detail_with_slider.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProductDetailDialog(object):
    def setupUi(self, ProductDetailDialog):
        ProductDetailDialog.setObjectName("ProductDetailDialog")
        ProductDetailDialog.resize(450, 650)
        ProductDetailDialog.setWindowTitle("")
        ProductDetailDialog.setStyleSheet("\n"
"QDialog {\n"
"    background-color: #fdfae6;\n"
"    border-radius: 16px;\n"
"}\n"
"QLabel#label_title {\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #5b4c2b;\n"
"}\n"
"QLabel#label_size {\n"
"    font-size: 14px;\n"
"    color: #7b9a79;\n"
"}\n"
"QLabel#label_price {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #5b4c2b;\n"
"}\n"
"QTextEdit#note_input {\n"
"    border: 1px solid #d8c49c;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton#btn_add_to_cart, QPushButton#btn_prev_image, QPushButton#btn_next_image {\n"
"    background-color: #fff9e9;\n"
"    border: 2px solid #d8c49c;\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"    color: #5b4c2b;\n"
"}\n"
"QPushButton#btn_add_to_cart:hover, QPushButton#btn_prev_image:hover, QPushButton#btn_next_image:hover {\n"
"    background-color: #f6eec7;\n"
"    border-color: #b89b6d;\n"
"}\n"
"   ")
        self.verticalLayout = QtWidgets.QVBoxLayout(ProductDetailDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(parent=ProductDetailDialog)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.label_size = QtWidgets.QLabel(parent=ProductDetailDialog)
        self.label_size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_size.setObjectName("label_size")
        self.verticalLayout.addWidget(self.label_size)
        self.stack_images = QtWidgets.QStackedWidget(parent=ProductDetailDialog)
        self.stack_images.setObjectName("stack_images")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.layout_image_0 = QtWidgets.QVBoxLayout(self.page_0)
        self.layout_image_0.setObjectName("layout_image_0")
        self.label_image = QtWidgets.QLabel(parent=self.page_0)
        self.label_image.setText("")
        self.label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.layout_image_0.addWidget(self.label_image)
        self.stack_images.addWidget(self.page_0)
        self.verticalLayout.addWidget(self.stack_images)
        self.layout_slider_btn = QtWidgets.QHBoxLayout()
        self.layout_slider_btn.setObjectName("layout_slider_btn")
        self.btn_prev_image = QtWidgets.QPushButton(parent=ProductDetailDialog)
        self.btn_prev_image.setObjectName("btn_prev_image")
        self.layout_slider_btn.addWidget(self.btn_prev_image)
        self.btn_next_image = QtWidgets.QPushButton(parent=ProductDetailDialog)
        self.btn_next_image.setObjectName("btn_next_image")
        self.layout_slider_btn.addWidget(self.btn_next_image)
        self.verticalLayout.addLayout(self.layout_slider_btn)
        self.label_description = QtWidgets.QLabel(parent=ProductDetailDialog)
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.label_price = QtWidgets.QLabel(parent=ProductDetailDialog)
        self.label_price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_price.setObjectName("label_price")
        self.verticalLayout.addWidget(self.label_price)
        self.note_input = QtWidgets.QTextEdit(parent=ProductDetailDialog)
        self.note_input.setObjectName("note_input")
        self.verticalLayout.addWidget(self.note_input)
        self.btn_back_to_cart = QtWidgets.QPushButton(parent=ProductDetailDialog)
        self.btn_back_to_cart.setObjectName("btn_back_to_cart")
        self.verticalLayout.addWidget(self.btn_back_to_cart)

        self.retranslateUi(ProductDetailDialog)
        QtCore.QMetaObject.connectSlotsByName(ProductDetailDialog)

    def retranslateUi(self, ProductDetailDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_title.setText(_translate("ProductDetailDialog", "Product Title"))
        self.label_size.setText(_translate("ProductDetailDialog", "12cm / 18cm"))
        self.btn_prev_image.setText(_translate("ProductDetailDialog", "< Prev"))
        self.btn_next_image.setText(_translate("ProductDetailDialog", "Next >"))
        self.label_description.setText(_translate("ProductDetailDialog", "Mô tả sản phẩm..."))
        self.label_price.setText(_translate("ProductDetailDialog", "480.000 VND"))
        self.note_input.setPlaceholderText(_translate("ProductDetailDialog", "Ghi chú thêm (tuỳ chọn)..."))
        self.btn_back_to_cart.setText(_translate("ProductDetailDialog", "Back to Cart +"))
