import datetime as dt
from typing import Optional
from pydantic import BaseModel, Field

class TradeDetails(BaseModel):
    buySellIndicator: str 
    price: float 
    quantity: int 

class Trade(BaseModel):
    asset_class: Optional[str]="N/A" 
    counterparty: Optional[str]="N/A"
    instrument_id: str 
    instrument_name: str 
    trade_date_time: dt.datetime 
    trade_details: TradeDetails 
    trade_id: str 
    trader: str 
