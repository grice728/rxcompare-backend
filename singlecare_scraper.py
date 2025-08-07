def scrape_singlecare(drug, dosage, quantity, zip_code):
    return {
        "source": "SingleCare",
        "drug": drug,
        "dosage": dosage,
        "quantity": quantity,
        "pharmacy": "CVS",
        "price": 8.50,
        "url": "https://www.singlecare.com"
    }
