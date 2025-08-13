# scoring.py
from typing import Optional
from models import PriceResult

def score_confidence(
    result: PriceResult,
    requested_strength_mg: Optional[float],
    requested_qty: Optional[int],
) -> PriceResult:
    score = 0
    notes = []

    # Drug name normalization match
    if result.norm_drug and result.norm_drug in (result.matched_drug_name or "").lower():
        score += 2
    else:
        notes.append("drug_name_loose")

    # Strength closeness
    if requested_strength_mg and result.norm_strength_mg:
        if abs(result.norm_strength_mg - requested_strength_mg) < 0.01:
            score += 2
        else:
            notes.append("strength_mismatch")

    # Quantity closeness
    if requested_qty and result.matched_pack_qty:
        diff = abs(result.matched_pack_qty - requested_qty)
        if diff == 0:
            score += 2
        elif diff <= 10:
            score += 1
            notes.append("qty_close")
        else:
            notes.append("qty_far")

    # URL presence is good
    if result.url:
        score += 1
    else:
        notes.append("no_url")

    # pharmacy present helps
    if result.pharmacy:
        score += 1

    conf = "low"
    if score >= 5:
        conf = "high"
    elif score >= 3:
        conf = "medium"

    result.confidence = conf  # type: ignore
    result.notes = ",".join(notes) if notes else None
    return result
