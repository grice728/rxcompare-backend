import csv
import os

def scrape_walmart(drug_name, dosage, quantity, zip_code):
    file_path = os.path.join(os.path.dirname(__file__), "walmart_4_dollar_list.csv")
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if drug_name.lower() == row["drug_name"].lower() and dosage == row["dosage"]:
                qty = int(quantity.split()[0])
                price = float(row["price_30"]) if qty <= 30 else float(row["price_90"])
                return {
                    "source": "Walmart $4 List",
                    "drug": drug_name,
                    "dosage": dosage,
                    "quantity": quantity,
                    "pharmacy": "Walmart",
                    "price": price,
                    "url": "https://www.walmart.com/pharmacy"
                }
    return {"error": "Not found on Walmart $4 list"}
