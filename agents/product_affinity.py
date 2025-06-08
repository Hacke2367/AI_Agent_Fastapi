import pandas as pd

class ProductAffinity:
    def __init__(self):
        self.affinity_map = {
            "Core Management Platform": ["Collaboration Suite", "Advanced Analytics"],
            "Collaboration Suite": ["Advanced Analytics", "Workflow Automation"],
            "Advanced Analytics": ["API Integrations", "Predictive Analytics"],
            "Workflow Automation": ["AI Insights Module", "Cloud Migration"],
            "Reporting Dashboard": ["API Integrations"],
            "API Integrations": ["IoT Monitoring", "Blockchain Security"],
            "AI Insights Module": ["Predictive Analytics"],
            "IoT Monitoring": ["Cloud Migration"],
            "Cloud Migration": ["Robotics Automation"],
            "Predictive Analytics": ["Telehealth Suite", "Content Analytics"],
            "Telehealth Suite": ["Blockchain Security"],
            "Robotics Automation": ["Predictive Maintenance"],
            "Blockchain Security": ["Supply Chain AI"],
            "Predictive Maintenance": ["AgriTech Sensors"],
            "Supply Chain AI": ["AgriTech Sensors"],
            "AgriTech Sensors": [],
            "Content Analytics": [],
        }
    def run(self, customer_profile: dict) -> dict:
        current_products = customer_profile.get("Current Products", "")
        product_list = [p.strip() for p in current_products.split(",") if p.strip()]

        recommended = set()

        for product in product_list:
            related = self.affinity_map.get(product, [])
            recommended.update(related)

        recommended -= set(product_list)

        return list(recommended)