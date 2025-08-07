def scrape_blink(drug, dosage, quantity, zip_code):
    return {
        "source": "Blink Health",
        "drug": drug,
        "dosage": dosage,
        "quantity": quantity,
        "pharmacy": "Walgreens",
        "price": 9.00,
        "url": "https://www.blinkhealth.com"
    }
