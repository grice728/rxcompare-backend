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
    for scraper in [
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
