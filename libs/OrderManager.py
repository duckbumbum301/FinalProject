import os
import json
import datetime
from models.order import Order
from models.order_detail import OrderDetail

class OrderManager:
    """
    Lớp quản lý chuyên biệt cho đơn hàng, 
    tách riêng khỏi DataConnector để tránh xung đột
    """
    
    def __init__(self, base_path="dataset"):
        self.base_path = base_path
        # Đảm bảo thư mục tồn tại
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        
        # Đường dẫn đến file orders.json
        self.orders_file = os.path.join(base_path, "orders.json")
        
        # Tạo file nếu chưa tồn tại
        if not os.path.exists(self.orders_file):
            with open(self.orders_file, 'w', encoding='utf-8') as f:
                f.write('[]')
                
    def get_all_orders(self):
        """
        Lấy tất cả đơn hàng từ file orders.json
        :return: Danh sách các Order
        """
        if not os.path.exists(self.orders_file):
            print(f"File {self.orders_file} does not exist")
            return []
            
        try:
            with open(self.orders_file, 'r', encoding='utf-8') as f:
                raw_data = f.read().strip()
                
            if not raw_data:
                print(f"File {self.orders_file} is empty")
                return []
                
            print(f"Reading orders from {self.orders_file}, raw data length: {len(raw_data)}")
            
            try:
                orders_data = json.loads(raw_data)
                
                if not isinstance(orders_data, list):
                    print(f"Invalid format in {self.orders_file}, expected a list")
                    return []
                    
                print(f"Successfully parsed JSON, found {len(orders_data)} orders")
                
                orders = []
                for order_dict in orders_data:
                    # Tạo đối tượng Order
                    order_items = order_dict.pop('items', []) if 'items' in order_dict else []
                    order = Order(**order_dict)
                    
                    # Tạo danh sách OrderDetail
                    items = []
                    for item_dict in order_items:
                        detail = OrderDetail(**item_dict)
                        items.append(detail)
                        
                    # Gán items vào order
                    order.items = items
                    orders.append(order)
                    
                return orders
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {str(e)}")
                return []
                
        except Exception as e:
            print(f"Error reading orders: {str(e)}")
            import traceback
            traceback.print_exc()
            return []
            
    def save_order(self, order, order_details):
        """
        Lưu đơn hàng mới hoặc cập nhật đơn hàng
        :param order: Đối tượng Order cần lưu
        :param order_details: Danh sách OrderDetail
        :return: Order đã lưu
        """
        print(f"=== ALTERNATIVE SAVE ORDER METHOD ===")
        # Gán items cho order
        order.items = order_details
        
        # Đảm bảo đơn hàng có ID
        if not order.order_id:
            # Tạo ID từ thời gian hiện tại để đảm bảo duy nhất
            current_time = datetime.datetime.now()
            order.order_id = f"CD{current_time.strftime('%Y%m%d%H%M%S')}"
            
        print(f"Saving order with ID: {order.order_id}")
        
        # Cập nhật order_id trong items
        for detail in order_details:
            detail.order_id = order.order_id
            
        # Lấy tất cả đơn hàng
        orders = self.get_all_orders()
        print(f"Current orders: {len(orders)}")
        
        # Kiểm tra đơn hàng đã tồn tại chưa
        order_exists = False
        for i, existing_order in enumerate(orders):
            if existing_order.order_id == order.order_id:
                orders[i] = order
                order_exists = True
                print(f"Updated existing order at index {i}")
                break
                
        # Thêm đơn hàng mới nếu chưa tồn tại
        if not order_exists:
            orders.append(order)
            print(f"Added new order")
            
        # Chuẩn bị dữ liệu để lưu
        json_data = []
        for o in orders:
            # Chuyển đổi Order thành dict
            order_dict = o.__dict__.copy()
            
            # Chuyển đổi items thành list dict
            if hasattr(o, 'items') and o.items:
                items_list = []
                for item in o.items:
                    items_list.append(item.__dict__)
                order_dict['items'] = items_list
                
            json_data.append(order_dict)
            
        # Lưu backup của file hiện tại
        if os.path.exists(self.orders_file):
            try:
                with open(self.orders_file, 'r', encoding='utf-8') as f:
                    old_data = f.read()
                backup_file = self.orders_file + '.backup'
                with open(backup_file, 'w', encoding='utf-8') as f:
                    f.write(old_data)
                print(f"Created backup at {backup_file}")
            except Exception as e:
                print(f"Failed to create backup: {str(e)}")
                
        # Lưu dữ liệu mới
        try:
            json_string = json.dumps(json_data, default=str, indent=4, ensure_ascii=False)
            with open(self.orders_file, 'w', encoding='utf-8') as f:
                f.write(json_string)
                
            print(f"Successfully saved {len(orders)} orders")
            
            # Xác minh file sau khi lưu
            try:
                with open(self.orders_file, 'r', encoding='utf-8') as f:
                    saved_data = f.read()
                print(f"Verification: File size after save: {len(saved_data)} bytes")
                
                if len(saved_data) < 10:
                    print(f"WARNING: File suspiciously small: {saved_data}")
                else:
                    verified_orders = json.loads(saved_data)
                    print(f"Verification: File contains {len(verified_orders)} orders")
            except Exception as e:
                print(f"Verification failed: {str(e)}")
                
            return order
            
        except Exception as e:
            print(f"Error saving orders: {str(e)}")
            import traceback
            traceback.print_exc()
            return order