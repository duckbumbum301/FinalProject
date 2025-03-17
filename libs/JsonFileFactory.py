import json
import os
class JsonFileFactory:
    def write_data(self,arr_data,filename):
        """
        Hàm này dùng để parse object thành jsonstring
        :param arr_data: mảng đối tượng
        :param filename:nơi lưu trữ jsonstring cho object
        :return: True nếu thành công
        """
        try:
            # Đảm bảo thư mục tồn tại
            directory = os.path.dirname(filename)
            if not os.path.exists(directory):
                os.makedirs(directory)
                
            if "orders.json" in filename:
                print(f"===== WRITE_DATA DEBUG for orders.json =====")
                print(f"Input arr_data contains {len(arr_data)} items")
                print(f"First few order IDs: {[item.order_id for item in arr_data[:3] if hasattr(item, 'order_id')]}")
            
            # Lưu backup nếu là file orders.json
            if "orders.json" in filename and os.path.exists(filename):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        old_data = f.read()
                    backup_file = filename + ".backup"
                    with open(backup_file, 'w', encoding='utf-8') as f:
                        f.write(old_data)
                    print(f"Backup file created at {backup_file}")
                    print(f"Backup file size: {len(old_data)} bytes")
                except Exception as e:
                    print(f"Failed to create backup: {e}")
                    
            # Ghi log số lượng item trước khi lưu
            print(f"Writing {len(arr_data)} items to {filename}")
                
            # Chuyển đổi dữ liệu sang JSON - xử lý đặc biệt với đối tượng có thuộc tính items
            json_array = []
            for item in arr_data:
                obj_dict = item.__dict__.copy()
                
                # Xử lý trường hợp đối tượng có thuộc tính items (Order với chi tiết đơn hàng)
                if 'items' in obj_dict and isinstance(obj_dict['items'], list):
                    # Chuyển đổi items thành danh sách dictionary
                    items_list = []
                    for detail_item in obj_dict['items']:
                        items_list.append(detail_item.__dict__)
                    obj_dict['items'] = items_list
                
                json_array.append(obj_dict)
                
            # Chuyển đổi sang JSON string
            json_string = json.dumps(json_array, default=str, indent=4, ensure_ascii=False)
            
            # Ghi file
            with open(filename, 'w', encoding='utf-8') as json_file:
                json_file.write(json_string)
                
            print(f"Successfully wrote data to {filename}")
            
            # Kiểm tra lại nội dung file sau khi ghi
            if "orders.json" in filename:
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        verification_data = f.read()
                    print(f"Verification: File size after write: {len(verification_data)} bytes")
                    
                    if len(verification_data) < 100:
                        print(f"WARNING: File content suspiciously small: {verification_data}")
                    else:
                        try:
                            # Kiểm tra xem có thể parse thành JSON không
                            json_obj = json.loads(verification_data)
                            print(f"Verification: Successfully parsed JSON, contains {len(json_obj)} items")
                        except json.JSONDecodeError as e:
                            print(f"Verification ERROR: Could not parse JSON: {str(e)}")
                except Exception as e:
                    print(f"Verification ERROR: Could not read file after write: {str(e)}")
                            
            return True
            
        except Exception as e:
            print(f"Error writing data to {filename}: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    def read_data(self,filename,ClassName):
        """
        Hàm đọc jsonstring và phục hồi lại mô hình lớp ClassName
        với ClassName là tên lớp được chỉ định phục hồi OOP
        :param filename: Đường dẫn tới file JSON
        :param ClassName: Lớp đối tượng cần khôi phục
        :return: Danh sách các đối tượng ClassName
        """
        try:
            if not os.path.isfile(filename):
                print(f"File {filename} does not exist, returning empty list")
                return []
                
            with open(filename, 'r', encoding='utf-8') as file:
                data = file.read()
                if not data.strip():  # Xử lý file trống
                    print(f"File {filename} is empty, returning empty list")
                    return []
                
                print(f"Reading JSON data from {filename}, content length: {len(data)}")
                
                # Parse JSON data
                json_data = json.loads(data)
                print(f"JSON data parsed, {len(json_data)} items found")
                
                # Xử lý đặc biệt cho Order với items
                result_objects = []
                for item_dict in json_data:
                    # Xử lý trường hợp đặc biệt của Order có items
                    if ClassName.__name__ == 'Order' and 'items' in item_dict:
                        from models.order_detail import OrderDetail
                        
                        # Sao chép dict để tránh sửa đổi bản gốc
                        order_dict = item_dict.copy()
                        
                        # Trích xuất items từ order_dict
                        items_data = order_dict.pop('items', [])
                        
                        # Tạo order mới từ dict đã loại bỏ items
                        obj = ClassName(**order_dict)
                        
                        # Chuyển đổi items thành OrderDetail objects
                        items_list = []
                        if isinstance(items_data, list):
                            for detail_dict in items_data:
                                detail_obj = OrderDetail(**detail_dict)
                                items_list.append(detail_obj)
                        
                        # Gán danh sách items vào order
                        obj.items = items_list
                    else:
                        # Xử lý các đối tượng khác
                        obj = ClassName(**item_dict)
                    
                    result_objects.append(obj)
                
                print(f"Successfully read {len(result_objects)} items from {filename}")
                return result_objects
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {filename}: {str(e)}")
            return []
        except Exception as e:
            print(f"Error reading data from {filename}: {str(e)}")
            import traceback
            traceback.print_exc()
            return []
    def validate_json_file(self, filename):
        """
        Kiểm tra nếu một file JSON hiện tại có định dạng hợp lệ
        :param filename: đường dẫn đến file JSON
        :return: True nếu file hợp lệ, False nếu không
        """
        if not os.path.exists(filename):
            print(f"File {filename} does not exist")
            return False
            
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                
                # Kiểm tra nếu file trống
                if not content:
                    print(f"File {filename} is empty")
                    return False
                    
                # Kiểm tra nếu nội dung không phải là JSON hợp lệ
                try:
                    json_data = json.loads(content)
                    
                    # Kiểm tra nếu không phải mảng JSON
                    if not isinstance(json_data, list):
                        print(f"File {filename} does not contain a JSON array")
                        return False
                        
                    print(f"File {filename} contains valid JSON array with {len(json_data)} items")
                    return True
                except json.JSONDecodeError as e:
                    print(f"File {filename} contains invalid JSON: {str(e)}")
                    return False
                    
        except Exception as e:
            print(f"Error validating JSON file {filename}: {str(e)}")
            return False