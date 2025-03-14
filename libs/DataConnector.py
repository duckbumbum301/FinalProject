import json
import os


class DataConnector:
    @staticmethod
    def load_products(file_path="products.json"):
        """Load products from JSON file"""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return []
        except Exception as e:
            print(f"Error loading products: {e}")
            return []

    @staticmethod
    def save_products(products, file_path="products.json"):
        """Save products to JSON file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(products, file, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Error saving products: {e}")
            return False