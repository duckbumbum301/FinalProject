import json

from test_cookies_writejson import cookies

from test_croissant_writejson import croissants

from test_drinks_writejson import drinks

from test_mousse_writejson import mousses

from test_tart_writejson import tarts

# Tạo một dictionary chứa tất cả các danh sách sản phẩm
products_data = {
    "cookies": cookies,
    "croissants": croissants,
    "drinks": drinks,
    "mousses": mousses,
    "tarts": tarts
}

# Đường dẫn lưu file JSON
filename = "products.json"
path = f"../dataset/{filename}"

# Ghi dữ liệu vào file JSON
with open(path, "w", encoding="utf-8") as file:
    json.dump(products_data, file, indent=4, ensure_ascii=False)

print(f"Data has been successfully saved to {path}")
