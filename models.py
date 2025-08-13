# models.py
from typing import Optional, Literal
from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime

Confidence = Literal["high", "medium", "low"]

class PriceResult(BaseModel):
    # Required
    source: str                       # e.g., "SingleCare", "Honeybee Health"
    pharmacy: Optional[str] = None    # e.g., "CVS", "Honeybee Health (Mail)"
    price: float                      # total price returned by source
    url: Optional[HttpUrl] = None

    # What the user asked for
    drug: str
    dosage: Optional[str] = None      # free text dosage from request
    quantity: Optional[str] = None    # free text quantity from request (e.g., "30 tablets")
    zip: Optional[str] = None

    # Normalized fields (for apples-to-apples)
    norm_drug: Optional[str] = None   # lowercased canonical name (generic preferred)
    norm_strength_mg: Optional[float] = None
    norm_form: Optional[str] = None   # tablet | capsule | solution | etc.
    norm_qty: Optional[int] = None    # integer count of units
    per_unit_price: Optional[float] = None

    # Matching diagnostics
    matched_drug_name: Optional[str] = None
    matched_strength_label: Optional[str] = None
    matched_pack_qty: Optional[int] = None   # pack size found at source
    closest_pack: Optional[int] = None       # closest pack size picked if exact unavailable
    confidence: Confidence = "low"
    notes: Optional[str] = None

    # Ops/observability
    source_last_checked_at: datetime = Field(default_factory=datetime.utcnow)
    scraper_version: Optional[str] = None
