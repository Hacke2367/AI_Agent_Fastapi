import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

class PurchasePattern:
    def __init__(self, usage_threshold: float = 70.0):
        self.usage_threshold = usage_threshold

    def run(self, customer_profile: dict) -> dict:
        current_product = customer_profile.get("Current Products", "")
        usage_percent = customer_profile.get("Product Usage (%)", 0)

        product_list = [p.strip() for p in current_product.split(",") if p.strip()]

        result = {
            "frequent_product": [],
            "missing_oppourtinites": []
        }

        if usage_percent >= self.usage_threshold:
            result["frequent_product"] = product_list
        else:
            result["missing_oppourtinites"] = product_list

        return result
