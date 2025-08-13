# normalize.py
import re
from typing import Optional, Tuple

UNIT_WORDS = {
    "tab": "tablet", "tabs": "tablet", "tablet": "tablet", "tablets": "tablet",
    "cap": "capsule", "caps": "capsule", "capsule": "capsule", "capsules": "capsule",
    "ml": "ml", "packet": "packet", "packets": "packet"
}

def _to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except Exception:
        return None

def parse_strength_mg(dosage: Optional[str]) -> Optional[float]:
    if not dosage:
        return None
    # handles "10mg", "12.5 mg", "100 mcg" (converts mcg -> mg), "1 g"
    s = dosage.lower().replace(" ", "")
    mg = re.search(r"([\d\.]+)mg", s)
    if mg:
        return _to_float(mg.group(1))
    mcg = re.search(r"([\d\.]+)mcg", s)
    if mcg:
        val = _to_float(mcg.group(1))
        return val/1000 if val is not None else None
    g = re.search(r"([\d\.]+)g", s)
    if g:
        val = _to_float(g.group(1))
        return val*1000 if val is not None else None
    return None

def parse_quantity(qty_text: Optional[str]) -> Optional[int]:
    if not qty_text:
        return None
    # "30", "30 tabs", "30 tablets", "Qty: 90", "90ct"
    m = re.search(r"(\d{1,5})", qty_text)
    if m:
        return int(m.group(1))
    return None

def parse_form(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    t = text.lower()
    for k, v in UNIT_WORDS.items():
        if re.search(rf"\b{k}\b", t):
            return v
    return None

def canonical_drug(drug: str) -> str:
    # Lowercase, strip, remove punctuation. (Later we can map brand->generic using a table.)
    return re.sub(r"[^a-z0-9 ]", "", drug.lower()).strip()

def choose_closest_pack(target_qty: Optional[int], candidates: list[int]) -> Optional[int]:
    if not target_qty or not candidates:
        return None
    best = None
    for c in candidates:
        if best is None or abs(c - target_qty) < abs(best - target_qty):
            best = c
    return best

def per_unit(total_price: float, pack_qty: Optional[int]) -> Optional[float]:
    if not pack_qty or pack_qty <= 0:
        return None
    try:
        return round(total_price / pack_qty, 4)
    except Exception:
        return None
