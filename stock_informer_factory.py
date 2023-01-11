from yahoofinance_informer import YahoofinanceStockInformer


class StockInformerFactory:
    @staticmethod
    def get_stock_informer(name='yahoo'):
        return {
            'yahoo': YahoofinanceStockInformer()
        }.get(name.lower())
