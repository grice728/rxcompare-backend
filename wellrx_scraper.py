def scrape_wellrx(drug, dosage, quantity, zip_code):
    return {
        "source": "WellRx",
        "drug": drug,
        "dosage": dosage,
        "quantity": quantity,
        "pharmacy": "Rite Aid",
        "price": 7.75,
        "url": "https://www.wellrx.com"
    }
