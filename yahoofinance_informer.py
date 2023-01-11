from stock_informer import AbstractStockInformer
import yfinance as yf
from typing import Optional
from models import StockDetails


class YahoofinanceStockInformer(AbstractStockInformer):

    @staticmethod
    def map_stock_details(ticker):
        mapper = {
            'sector': 'industry',
            'recommendationKey': 'recommendation_status',
            'sharesOutstanding': 'number_of_shares',
            'regularMarketPrice': 'price',
            'shortName': 'short_name'
        }
        output = {mapper[k]: ticker.info[k] for k in mapper}
        return StockDetails(**output)

    def get_stock_details(self, stock_ticker_symbol) -> Optional[StockDetails]:
        ticker = yf.Ticker(stock_ticker_symbol)

        if not ticker.info:
            return None

        stock_details = YahoofinanceStockInformer.map_stock_details(ticker)

        return stock_details

    def get_stock_price(self, stock_ticker_symbol) -> Optional[float]:
        stock_details = self.get_stock_details(stock_ticker_symbol)
        if stock_details:
            return float(stock_details.price)
        return None


if __name__ == '__main__':
    yf_broker = YahoofinanceStockInformer()
    for i in range(100):
        pltr_details = yf_broker.get_stock_details('pltr')
        print(pltr_details)
        print(pltr_details.price)
