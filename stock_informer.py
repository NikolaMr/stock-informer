from abc import ABC, abstractmethod
from typing import Optional
from models import StockDetails

class AbstractStockInformer(ABC):

    @abstractmethod
    def get_stock_price(self, stock_ticker_symbol) -> Optional[float]:
        pass

    @abstractmethod
    def get_stock_details(self, stock_ticker_symbol) -> Optional[StockDetails]:
        pass
