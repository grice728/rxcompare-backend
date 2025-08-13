# scrapers/costplus.py
from typing import List
from models import PriceResult

def scrape(drug: str, dosage: str, quantity: str, zip_code: str) -> List[PriceResult]:
    """
    TODO: implement real scraping for Cost Plus Drugs.
    Return a list of PriceResult objects (can be >1 if multiple pharmacies or packs).
    For now, return [] so we don't show placeholders.
    """
    return []
