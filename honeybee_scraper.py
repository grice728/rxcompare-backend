def scrape_honeybee(drug, dosage, quantity, zip_code):
    return {
        "source": "Honeybee Health",
        "drug": drug,
        "dosage": dosage,
        "quantity": quantity,
        "pharmacy": "Honeybee Health (Mail Order)",
        "price": 5.75,
        "url": "https://www.honeybeehealth.com"
    }
