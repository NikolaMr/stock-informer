from fastapi import FastAPI
from stock_informer_factory import StockInformerFactory
from models import StockDetails

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache

app = FastAPI()


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


@app.get("/stocks/details/{stock_ticker_symbol}", response_model=StockDetails)
@cache(expire=60)
async def stock_details(stock_ticker_symbol: str):
    return StockInformerFactory.get_stock_informer().get_stock_details(stock_ticker_symbol)


@app.get("/stocks/price/{stock_ticker_symbol}", response_model=float)
@cache(expire=60)
async def stock_price(stock_ticker_symbol: str):
    return StockInformerFactory.get_stock_informer().get_stock_price(stock_ticker_symbol)
