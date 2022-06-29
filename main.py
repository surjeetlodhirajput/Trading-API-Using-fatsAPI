from fastapi import FastAPI,HTTPException,Body
from models import Trade,TradeDetails
from typing import List,Optional,Union
import datetime as datetime,time
from uuid import UUID,uuid4
from pydantic import BaseModel
import random
import randomData as rd
db: List[Trade]=[
Trade(
asset_class="Stocks",
counterparty="Individual Investor",
instrument_id="TSLA",
instrument_name="Tesla Shorting Losers Association",
trade_date_time=datetime.datetime(2020,5,18),
trade_details=
TradeDetails(
buySellIndicator="BUY",
price=1292390898.2487,
quantity=20
),
trade_id="100",
trader="surjeet Rajput"
),
]
random_start_date=datetime.datetime(2000,1,1)
random_end_date=datetime.datetime.today()
id_=1
for i in range(2,10):
    time_between_dates = random_end_date - random_start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = random_start_date + datetime.timedelta(days=random_number_of_days)
    i_id=rd.instrument_id[random.randint(0,(len(rd.instrument_id)-1))]
    db.append(Trade(
        asset_class=rd.assest_values[random.randint(0,3)],
        counterparty=["Individual party",'Government','N/A'][random.randint(0,2)],
        instrument_id=i_id,
        instrument_name=rd.instrument_name[i_id],
        trade_date_time=random_date,
        trade_details=
        TradeDetails(
        buySellIndicator=rd.buySellIndicator[random.randint(0,1)],
        price=random.randint(1000,1000000000),
        quantity=random.randint(1,100)),
        trade_id=str(id_),
        trader=rd.first_name[random.randint(0,(len(rd.first_name)-1))]+" "+rd.last_name[random.randint(0,5)])
    ) 
    id_+=1
app=FastAPI()
@app.get('/')#root path
def root():
    return "For fetching trades list please visit /trades"
@app.get('/trades')
def fetch_trades(): #fetching all trade
    return  db
@app.get('/trades/{trade_id}')
def fetch_trade_by_id(trade_id:str): #fetching trade using the id of the trade
    for trade in db:
        if trade.trade_id==trade_id:
            return trade
    raise HTTPException(status_code=404, detail="trade not found")

@app.get('/search-trades')#query search
def search_trade(search:str): #for searching the query as respect to counterpart,trader,instrumetnname and instrumentid
    for trade in db:
        if trade.counterparty.lower().__contains__(search.lower()):
            return trade
        elif trade.trader.lower().__contains__(search.lower()):
            return trade
        elif trade.instrument_id.lower().__contains__(search.lower()):
            return trade
        elif trade.instrument_name.lower().__contains__(search.lower()):
            return trade
    raise HTTPException(status_code=404, detail="trade not found")

@app.get('/filter-trades') #function for filtering the trade all min and max value are required while assest_class and tradeType is optional
def filter_trade(minPrice:float,maxPrice:float,start:datetime.datetime,end:datetime.datetime,asset_class:str="N/A",tradeType:str="N/A"):
    data=[]
    if asset_class!="N/A" and tradeType!="N/A":
        for trade in db:
            if trade.trade_details.price>=minPrice and trade.trade_details.price<=maxPrice and trade.trade_date_time>=start and trade.trade_date_time<=end and trade.asset_class==asset_class and trade.trade_details.buySellIndicator==tradeType:
                data.append(trade)
    if asset_class=="N/A" and tradeType!="N/A":
        for trade in db:
            if trade.trade_details.price>=minPrice and trade.trade_details.price<=maxPrice and trade.trade_date_time>=start and trade.trade_date_time<=end and trade.trade_details.buySellIndicator==tradeType:
                data.append(trade)
    if asset_class!="N/A" and tradeType=="N/A":
        for trade in db:
            if trade.trade_details.price>=minPrice and trade.trade_details.price<=maxPrice and trade.trade_date_time>=start and trade.trade_date_time<=end and trade.asset_class==asset_class:
                data.append(trade)
    if asset_class=="N/A" and tradeType=="N/A":
        for trade in db:
            if trade.trade_details.price>=minPrice and trade.trade_details.price<=maxPrice and trade.trade_date_time>=start and trade.trade_date_time<=end:
                data.append(trade)
    if data!=[]:
        return data
    else:
        raise HTTPException(status_code=404, detail="trade not found")

@app.get('/pagination')#this function will sort the trades on the basis of their trade id
def pagination(page:int,resultPerPage:int):
    start_from=(page-1)*resultPerPage
    ans=[]
    l=len(db)
    if start_from<l and (resultPerPage+start_from)<l:
        ans=db[start_from:(start_from+resultPerPage)]
    elif start_from<l: 
        ans=db[start_from:]

    if ans!=[]:
        return ans
    else: 
        raise HTTPException(status_code=404, detail="trade not found")

@app.get('/sort-trades')
def sort_trades():
    db.sort(key=lambda x:int(x.trade_id),reverse=False)
    return db
@app.post('/create-trade/')#route for creating the new trade details
def create_trade(trade:Trade):
    for trad in db:
        if trad.trade_id==trade.trade_id:
            raise HTTPException(status_code=409, detail="trade id already exist")
    db.append(trade)
    return trade
