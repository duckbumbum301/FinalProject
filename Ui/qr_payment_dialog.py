from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import segno
import os
import tempfile


class QRPaymentDialog(QDialog):
    def __init__(self, order_id, total_amount, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Thanh Toán Online")
        self.setFixedSize(400, 500)

        # Tạo layout chính
        layout = QVBoxLayout()

        # Tạo label hướng dẫn
        instruction_label = QLabel("Vui lòng quét mã QR để thanh toán")
        instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instruction_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #5b4c2b; margin: 10px;")
        layout.addWidget(instruction_label)

        # Tạo label hiển thị thông tin đơn hàng
        order_info = QLabel(f"Mã đơn hàng: {order_id}\nTổng tiền: {total_amount:,} VNĐ")
        order_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        order_info.setStyleSheet("font-size: 14px; color: #5b4c2b; margin: 10px;")
        layout.addWidget(order_info)

        try:
            # Tạo nội dung QR code
            qr_data = f"order_id={order_id}&amount={total_amount}"
            
            # Tạo file QR code tạm thời
            temp_dir = tempfile.gettempdir()
            qr_file = os.path.join(temp_dir, f"qr_code_{order_id}.png")
            
            # Tạo QR code sử dụng segno
            qr = segno.make(qr_data)
            qr.save(qr_file, scale=10)
            
            # Hiển thị QR code
            qr_pixmap = QPixmap(qr_file)
            qr_label = QLabel()
            qr_label.setPixmap(qr_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
            qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(qr_label)
            
            # Xóa file tạm sau khi đã load
            os.remove(qr_file)
            
        except Exception as e:
            # Nếu có lỗi, hiển thị thông báo lỗi
            error_label = QLabel("Không thể tạo mã QR. Vui lòng thử lại sau.")
            error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            error_label.setStyleSheet("color: red; font-size: 14px;")
            layout.addWidget(error_label)
            print(f"Error creating QR code: {str(e)}")

        # Tạo nút đóng
        close_button = QPushButton("Đóng")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(251, 236, 207);
                color: rgb(91, 76, 43);
                border-radius: 15px;
                padding: 8px;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: rgb(216, 203, 164);
            }
        """)
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        self.setLayout(layout) 