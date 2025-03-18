from libs.JsonFileFactory import JsonFileFactory
import os
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_detail import OrderDetail


class DataConnector:
    def __init__(self):
        self.jff = JsonFileFactory()
        self.base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dataset")

        # Đảm bảo thư mục dataset tồn tại
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    # === PRODUCT METHODS ===
    def get_all_products(self):
        filename = os.path.join(self.base_path, "products.json")
        try:
            products = self.jff.read_data(filename, Product)
            return products
        except:
            return []

    def save_product(self, product):
        products = self.get_all_products()

        # Chuyển đổi sản phẩm về lớp Product cơ bản
        if not isinstance(product, Product):
            basic_product = Product(
                product_id=product.product_id,
                name=product.name,
                price=product.price,
                quantity=product.quantity,
                notes=product.notes if hasattr(product, 'notes') else None,
                category=product.__class__.__name__,  # Lưu tên lớp làm category
                description=product.description if hasattr(product, 'description') else None,
                image_path=product.image_path if hasattr(product, 'image_path') else None
            )
            product = basic_product

        # Kiểm tra nếu sản phẩm đã tồn tại thì cập nhật
        index = self.find_product_index(product.product_id)
        if index != -1:
            products[index] = product
        else:
            products.append(product)

        filename = os.path.join(self.base_path, "products.json")
        self.jff.write_data(products, filename)
        return product

    def find_product_index(self, product_id):
        products = self.get_all_products()
        for i, product in enumerate(products):
            if product.product_id == product_id:
                return i
        return -1

    def find_product_by_id(self, product_id):
        products = self.get_all_products()
        for product in products:
            if product.product_id == product_id:
                return product
        return None

    def delete_product(self, product_id):
        products = self.get_all_products()
        index = self.find_product_index(product_id)
        if index != -1:
            products.pop(index)
            filename = os.path.join(self.base_path, "products.json")
            self.jff.write_data(products, filename)
            return True
        return False

    # === CUSTOMER METHODS ===
    def get_all_customers(self):
        filename = os.path.join(self.base_path, "customers.json")
        try:
            customers = self.jff.read_data(filename, Customer)
            return customers
        except:
            return []

    def save_customer(self, customer):
        customers = self.get_all_customers()
        
        # Nếu đã có customer_id hợp lệ (từ find_customer_by_phone), giữ nguyên ID
        # Ngược lại, tạo ID mới
        if not customer.customer_id or not customer.customer_id.startswith("VA"):
            customer.customer_id = self.generate_customer_id()
            print(f"Generated new customer ID: {customer.customer_id}")

        # Kiểm tra xem customer có tồn tại trong danh sách hiện tại không
        # dựa trên ID
        customer_exists = False
        for i, existing_customer in enumerate(customers):
            if existing_customer.customer_id == customer.customer_id:
                customers[i] = customer
                customer_exists = True
                print(f"Updating existing customer with ID: {customer.customer_id}")
                break
        
        # Nếu không tìm thấy khách hàng, thêm mới
        if not customer_exists:
            customers.append(customer)
            print(f"Adding new customer with ID: {customer.customer_id}")

        # Lưu danh sách khách hàng
        filename = os.path.join(self.base_path, "customers.json")
        print(f"Saving {len(customers)} customers to {filename}")
        self.jff.write_data(customers, filename)
        return customer

    def find_customer_index(self, customer_id):
        customers = self.get_all_customers()
        for i, customer in enumerate(customers):
            if customer.customer_id == customer_id:
                return i
        return -1

    def find_customer_by_id(self, customer_id):
        customers = self.get_all_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def find_customer_by_phone(self, phone):
        customers = self.get_all_customers()
        for customer in customers:
            if customer.phone == phone:
                return customer
        return None

    def delete_customer(self, customer_id):
        customers = self.get_all_customers()
        index = self.find_customer_index(customer_id)
        if index != -1:
            customers.pop(index)
            filename = os.path.join(self.base_path, "customers.json")
            self.jff.write_data(customers, filename)
            return True
        return False

    # === ORDER METHODS ===
    def get_all_orders(self):
        """
        Lấy tất cả đơn hàng từ file orders.json
        :return: Danh sách các Order
        """
        filename = os.path.join(self.base_path, "orders.json")
        
        if not os.path.exists(filename):
            print(f"File orders.json does not exist at {filename}")
            return []
            
        print(f"Reading orders from: {filename}")
        
        try:
            # Đọc nội dung thô của file để kiểm tra
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                print(f"Raw file content length: {len(raw_content)}")
                if len(raw_content) < 100:
                    print(f"Raw content: {raw_content}")
                else:
                    print(f"First 100 chars: {raw_content[:100]}...")
            except Exception as e:
                print(f"Error reading raw content: {e}")
            
            # Tiếp tục đọc bằng JsonFileFactory
            orders = self.jff.read_data(filename, Order)
            if orders:
                order_ids = [order.order_id for order in orders]
                print(f"Successfully read {len(orders)} orders with IDs: {order_ids}")
            else:
                print("No orders found in file")
            return orders
        except Exception as e:
            print(f"Error reading orders: {str(e)}")
            import traceback
            traceback.print_exc()
            return []

    def save_order(self, order, order_details):
        """
        Lưu đơn hàng và chi tiết đơn hàng
        :param order: đối tượng Order cần lưu
        :param order_details: danh sách OrderDetail thuộc order
        :return: Order đã được lưu
        """
        # Đảm bảo order có ID
        if not order.order_id:
            order.order_id = self.generate_order_id()

        print(f"=== Starting order save process for ID {order.order_id} ===")

        # Gán chi tiết đơn hàng vào đơn hàng
        order.items = order_details

        # Cập nhật order_id trong chi tiết đơn hàng
        for detail in order_details:
            detail.order_id = order.order_id

        # Lấy danh sách đơn hàng hiện có
        orders = self.get_all_orders()
        print(f"Current orders count before save: {len(orders)}")
        if orders:
            print(f"Existing order IDs: {[order.order_id for order in orders]}")

        # Kiểm tra nếu đơn hàng đã tồn tại thì cập nhật
        order_exists = False
        for i, existing_order in enumerate(orders):
            if existing_order.order_id == order.order_id:
                print(f"Replacing order at index {i}")
                orders[i] = order
                order_exists = True
                print(f"Updating existing order: {order.order_id}")
                break

        # Nếu không tồn tại thì thêm mới
        if not order_exists:
            print(f"Adding new order with ID {order.order_id} to the list")
            orders.append(order)
            print(f"New orders list length: {len(orders)}")

        # Kiểm tra lại danh sách orders sau khi thêm
        check_ids = [o.order_id for o in orders]
        print(f"All order IDs before saving: {check_ids}")
        if check_ids.count(order.order_id) > 1:
            print(f"WARNING: Duplicate order ID {order.order_id} found in list!")

        # Lưu danh sách vào file
        filename = os.path.join(self.base_path, "orders.json")
        print(f"Saving {len(orders)} orders to {filename}")
        success = self.jff.write_data(orders, filename)
        print(f"Save to {filename} result: {success}")
        print(f"Total orders after save: {len(orders)}")
        print(f"=== Order save process completed ===")

        return order

    def get_order_by_id(self, order_id):
        orders = self.get_all_orders()
        for order in orders:
            if order.order_id == order_id:
                return order
        return None

    def get_orders_by_customer_id(self, customer_id):
        orders = self.get_all_orders()
        return [order for order in orders if order.customer_id == customer_id]

    def update_order_status(self, order_id, new_status):
        orders = self.get_all_orders()
        for order in orders:
            if order.order_id == order_id:
                order.status = new_status
                filename = os.path.join(self.base_path, "orders.json")
                self.jff.write_data(orders, filename)
                return True
        return False

    def delete_order(self, order_id):
        orders = self.get_all_orders()
        for i, order in enumerate(orders):
            if order.order_id == order_id:
                orders.pop(i)
                filename = os.path.join(self.base_path, "orders.json")
                self.jff.write_data(orders, filename)
                return True
        return False

    # === ORDER DETAIL METHODS ===
    def get_order_details_by_order_id(self, order_id):
        # Trong triển khai hiện tại, chi tiết đơn hàng được lưu trong đơn hàng
        order = self.get_order_by_id(order_id)
        if order and hasattr(order, 'items'):
            return order.items
        return []

    # === STATISTICS METHODS ===
    def get_total_sales(self):
        orders = self.get_all_orders()
        return sum(order.total_amount for order in orders)

    def get_total_sales_by_date(self, date_str):
        orders = self.get_all_orders()
        return sum(order.total_amount for order in orders if order.order_date.startswith(date_str))

    def get_bestselling_products(self, limit=10):
        # Tạo một dict để đếm số lượng bán ra cho mỗi sản phẩm
        product_sales = {}
        orders = self.get_all_orders()

        for order in orders:
            if hasattr(order, 'items'):
                for item in order.items:
                    if item.product_id in product_sales:
                        product_sales[item.product_id] += item.quantity
                    else:
                        product_sales[item.product_id] = item.quantity

        # Sắp xếp theo số lượng bán giảm dần
        sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

        # Giới hạn số lượng kết quả trả về
        top_products = sorted_products[:limit]

        # Lấy thông tin chi tiết của sản phẩm
        result = []
        for product_id, quantity in top_products:
            product = self.find_product_by_id(product_id)
            if product:
                result.append({
                    'product': product,
                    'quantity_sold': quantity
                })

        return result

    # === UTILITY METHODS ===
    def generate_id(self):
        """Tạo ID ngẫu nhiên"""
        import uuid
        return str(uuid.uuid4())
        
    def generate_customer_id(self):
        """Tạo Customer ID theo định dạng VA{i} với i tăng dần"""
        customers = self.get_all_customers()
        
        # Nếu không có khách hàng, bắt đầu từ VA1
        if not customers:
            return "VA1"
            
        # Tìm số thứ tự lớn nhất hiện tại
        max_customer_num = 0
        for customer in customers:
            if customer.customer_id and customer.customer_id.startswith("VA"):
                try:
                    customer_num = int(customer.customer_id[2:])  # Lấy phần số sau "VA"
                    max_customer_num = max(max_customer_num, customer_num)
                except ValueError:
                    # Bỏ qua nếu không phải định dạng VA+số
                    pass
                    
        # Tạo ID mới bằng cách tăng số thứ tự lên 1
        new_customer_num = max_customer_num + 1
        return f"VA{new_customer_num}"

    def generate_order_id(self):
        """Tạo Order ID theo định dạng CD{i} với i tăng dần"""
        orders = self.get_all_orders()

        # Nếu không có đơn hàng, bắt đầu từ CD1
        if not orders:
            return "CD1"

        # Tìm số thứ tự lớn nhất hiện tại
        max_order_num = 0
        for order in orders:
            if order.order_id and order.order_id.startswith("CD"):
                try:
                    order_num = int(order.order_id[2:])  # Lấy phần số sau "CD"
                    max_order_num = max(max_order_num, order_num)
                except ValueError:
                    # Bỏ qua nếu không phải định dạng CD+số
                    pass

        # Tạo ID mới bằng cách tăng số thứ tự lên 1
        new_order_num = max_order_num + 1
        return f"CD{new_order_num}"