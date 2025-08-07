def scrape_costplus(drug, dosage, quantity, zip_code):
    return {
        "source": "Cost Plus Drugs",
        "drug": drug,
        "dosage": dosage,
        "quantity": quantity,
        "pharmacy": "Mark Cuban Cost Plus",
        "price": 6.00,
        "url": "https://www.costplusdrugs.com"
    }
