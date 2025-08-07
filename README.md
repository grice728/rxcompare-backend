# RxCompare Backend

This is the FastAPI backend for RxCompare. It provides drug price comparison from multiple pharmacy discount providers.

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## POST /api/search

Example payload:
```json
{
  "drug": "atorvastatin",
  "dosage": "10mg",
  "quantity": "30 tablets",
  "zip": "10001"
}
```

Returns best price and list of results.
