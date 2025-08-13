from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from singlecare_scraper import scrape_singlecare
from blink_scraper import scrape_blink
from wellrx_scraper import scrape_wellrx
from costplus_scraper import scrape_costplus
from walmart_scraper import scrape_walmart
from costco_scraper import scrape_costco
from honeybee_scraper import scrape_honeybee

# --- RXCOMPARE SCRAPER IMPORTS (safe) ---
try:
    from scrapers.costplus import scrape as scrape_costplus
except Exception:
    scrape_costplus = None

try:
    from scrapers.singlecare import scrape as scrape_singlecare
except Exception:
    scrape_singlecare = None

try:
    from scrapers.wellrx import scrape as scrape_wellrx
except Exception:
    scrape_wellrx = None

# Enable these later when real & tested:
# try:
#     from scrapers.honeybee import scrape as scrape_honeybee
# except Exception:
#     scrape_honeybee = None
# try:
#     from scrapers.blink import scrape as scrape_blink
# except Exception:
#     scrape_blink = None
# --- END SCRAPER IMPORTS ---
# --- RXCOMPARE ENABLED SCRAPERS ---
SCRAPER_FUNCS = []
for fn in (scrape_costplus, scrape_singlecare, scrape_wellrx):
    if callable(fn):
        SCRAPER_FUNCS.append(fn)

# Later, when verified:
# for fn in (scrape_honeybee, scrape_blink):
#     if callable(fn):
#         SCRAPER_FUNCS.append(fn)

# Optional: print which scrapers are active at startup (helps debugging)
try:
    print("[RxCompare] Enabled scrapers:", [getattr(fn, "__name__", "fn") for fn in SCRAPER_FUNCS])
except Exception:
    pass
# --- END ENABLED SCRAPERS ---

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DrugRequest(BaseModel):
    drug: str
    dosage: str
    quantity: str
    zip: str

@app.post("/api/search")
async def search_prices(req: DrugRequest):
    results = []
    for scraper_funcs in [
        scrape_singlecare, scrape_blink, scrape_wellrx,
        scrape_costplus, scrape_walmart, scrape_costco,
        scrape_honeybee
    ]:
        try:
            result = scraper(req.drug, req.dosage, req.quantity, req.zip)
            if result and "price" in result and result["price"] > 0:
                results.append(result)
        except:
            continue
    if not results:
        return {"error": "No prices found"}
    return {
        "best_price": min(results, key=lambda x: x["price"]),
        "all_results": results
    }
