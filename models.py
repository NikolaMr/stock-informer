from pydantic import BaseModel


class StockDetails(BaseModel):
    industry: str
    recommendation_status: str
    number_of_shares: int
    price: float
    short_name: str
