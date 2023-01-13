from fastapi import FastAPI, HTTPException
from stock_informer_factory import StockInformerFactory
from models import StockDetails

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache

app = FastAPI()


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


@app.get(
    "/stocks/details/{stock_ticker_symbol}",
    response_model=StockDetails,
    description='This endpoint fetches details for a stock with the given ticker symbol.',
    responses={
        404: {
            'description': 'Ticker symbol not found.'
        }
    }
)
@cache(expire=60)
async def stock_details(stock_ticker_symbol: str):
    details = StockInformerFactory.get_stock_informer().get_stock_details(stock_ticker_symbol)
    if details is not None:
        return details
    raise HTTPException(status_code=404, detail='Ticker symbol not found.')


@app.get(
    "/stocks/price/{stock_ticker_symbol}",
    response_model=float,
    description='This endpoint fetches the price of the stock with the given ticker symbol',
    responses={
        404: {
            'description': 'Ticker symbol not found.'
        }
    }
)
@cache(expire=60)
async def stock_price(stock_ticker_symbol: str):
    price = StockInformerFactory.get_stock_informer().get_stock_price(stock_ticker_symbol)
    if price is not None:
        return price
    raise HTTPException(status_code=404, detail='Ticker symbol not found.')


@app.get(
    "/health",
    response_model=str,
    description='This endpoint can be reached out to check if the server is working as expected. '
                'For now, it just returns "working" to indicate so.'
)
async def health_check():
    return 'working'
