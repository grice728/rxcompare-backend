def scrape_costco(drug, dosage, quantity, zip_code):
    return {
        "source": "Costco",
        "drug": drug,
        "dosage": dosage,
        "quantity": quantity,
        "pharmacy": "Costco Pharmacy",
        "price": 7.00,
        "url": "https://www.costco.com/pharmacy"
    }
