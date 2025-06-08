from dotenv import load_dotenv
import pandas as pd
import numpy as np
from data import *
import pdfplumber

with pdfplumber.open("Data/customer_data.pdf") as pdf:
    all_data = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_data.append(df)
final_df = pd.concat(all_data, ignore_index=True)
final_df.to_csv("data/customer_data.csv", index=False)

import pandas as pd

class CustomerContextAgent:
    def __init__(self, data_path: str = "data/customer_data.csv"):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)

    def run(self, customer_id: str) -> dict:
        customer_row = self.df[self.df["Customer ID"] == customer_id]

        if customer_row.empty:
            raise ValueError(f"Customer ID '{customer_id}' not found")

        profile = customer_row.iloc[0].to_dict()
        return profile




