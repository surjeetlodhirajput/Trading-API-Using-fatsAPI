# Rest Api Application
this api is develop using fastapi,typing,pydantic and datatime
this api will generate data for trades
## Install
    git clone https://github.com/surjeetlodhirajput/Trading-API-Using-fatsAPI.git 

## Run the app

    unicorn main:app --reload

# REST API

The REST API to the trade app is described below.
### Request

`GET /`

curl -X 'GET' \ 'http://localhost:8000/' \ -H 'accept: application/json'
### Response
    
     content-length: 47 
     content-type: application/json 
     date: Wed,29 Jun 2022 09:17:34 GMT 
     server: uvicorn 
    
    "For fetching trades list please visit /trades"


### Request

`GET /trades`


curl -X 'GET' \ 'http://localhost:8000/trades' \ -H 'accept: application/json'
### Response

    content-length: 1991 
    content-type: application/json 
    date: Wed,29 Jun 2022 09:20:55 GMT 
    server: uvicorn 
    "[
  {
    "asset_class": "Stocks",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-05-18T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 1292390898.2487,
      "quantity": 20
    },
    "trade_id": "1",
    "trader": "surjeet Rajput"
  },
  {
    "asset_class": "Equities",
    "counterparty": "Individual Investor",
    "instrument_id": "AMZN",
    "instrument_name": "Amazon",
    "trade_date_time": "2022-01-08T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 9920898.287,
      "quantity": 10
    },
    "trade_id": "100",
    "trader": "Rajiv mahey"
  },
  {
    "asset_class": "Fixed Income",
    "counterparty": "Government",
    "instrument_id": "AAPL",
    "instrument_name": "American Association of Professional Landmen.",
    "trade_date_time": "2021-10-31T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 90772773.9,
      "quantity": 2
    },
    "trade_id": "12",
    "trader": "Nella Nirjalla"
  },
  {
    "asset_class": "Bonds",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-09-28T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 6389127389.27,
      "quantity": 4
    },
    "trade_id": "199",
    "trader": "Gautam Gangully"
  },
  {
    "asset_class": "Stocks",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2015-02-12T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 7281273712,
      "quantity": 12
    },
    "trade_id": "177",
    "trader": "bob smith"
  },
  {
    "asset_class": "N/A",
    "counterparty": "N/A",
    "instrument_id": "AMZN",
    "instrument_name": "Amazon",
    "trade_date_time": "2005-04-12T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 7281272,
      "quantity": 9
    },
    "trade_id": "177",
    "trader": "Rana tunga"
  },
  {
    "asset_class": "Stocks",
    "counterparty": "Individual",
    "instrument_id": "AMZN",
    "instrument_name": "Amazon",
    "trade_date_time": "2022-06-29T09:05:24.996000+00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 1920102,
      "quantity": 10
    },
    "trade_id": "10",
    "trader": "Bana babu"
  }
]"

## Get a specific trade

### Request

`GET /trades/trade_id`

    curl -X 'GET' \ 'http://localhost:8000/trades/10' \ -H 'accept: application/json'

### Response

    content-length: 268 
    content-type: application/json 
    date: Wed,29 Jun 2022 09:25:27 GMT 
    server: uvicorn 

    {
  "asset_class": "Stocks",
  "counterparty": "Individual",
  "instrument_id": "AMZN",
  "instrument_name": "Amazon",
  "trade_date_time": "2022-06-29T09:05:24.996000+00:00",
  "trade_details": {
    "buySellIndicator": "SELL",
    "price": 1920102,
    "quantity": 10
     },
     "trade_id": "10",
    "trader": "Bana babu"
    }


## Get a non-existent trade

### Request

`GET /trades/trade_id`

    curl -X 'GET' \ 'http://localhost:8000/trades/11' \ -H 'accept: application/json'

### Response

    content-length: 28 
    content-type: application/json 
    date: Wed,29 Jun 2022 09:27:37 GMT 
    server: uvicorn 
    {
  "detail": "trade not found"
    }

## Create another new trade

### Request

`POST /create-trade/`

curl -X 'POST' \ 'http://localhost:8000/create-trade/' \ -H 'accept: application/json' \ -H 'Content-Type: application json' \
  -d '{
  "asset_class": "Stocks",
  "counterparty": "Individual",
  "instrument_id": "AMZN",
  "instrument_name": "Amazon",
  "trade_date_time": "2022-06-29T09:05:24.996Z",
  "trade_details": {
    "buySellIndicator": "SELL",
    "price": 1920102,
    "quantity": 10
  },
  "trade_id": "110",
  "trader": "Bana babu"
}'
### Response

 content-length: 269 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:29:22 GMT 
 server: uvicorn 

{
  "asset_class": "Stocks",
  "counterparty": "Individual",
  "instrument_id": "AMZN",
  "instrument_name": "Amazon",
  "trade_date_time": "2022-06-29T09:05:24.996000+00:00",
  "trade_details": {
    "buySellIndicator": "SELL",
    "price": 1920102,
    "quantity": 10
  },
  "trade_id": "110",
  "trader": "Bana babu"
}
## creating existing trade 
### Request

`POST /create-trade/`

curl -X 'POST' \ 'http://localhost:8000/create-trade/' \ -H 'accept: application/json' \ -H 'Content-Type: application json' \
  -d '{
  "asset_class": "Stocks",
  "counterparty": "Individual",
  "instrument_id": "AMZN",
  "instrument_name": "Amazon",
  "trade_date_time": "2022-06-29T09:05:24.996Z",
  "trade_details": {
    "buySellIndicator": "SELL",
    "price": 1920102,
    "quantity": 10
  },
  "trade_id": "110",
  "trader": "Bana babu"
}'
### Response

 content-length: 35 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:35:06 GMT 
 server: uvicorn 
 {
  "detail": "trade id already exist"
 }

## searching trade 
### Request

`GET /search-trades/`

curl -X 'GET' \ 'http://localhost:8000/search-trades?search=bob%20smith' \ H 'accept: application/json' json' \
  
### Response

 content-length: 294 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:37:49 GMT 
 server: uvicorn 

 {
  "asset_class": "Stocks",
  "counterparty": "Individual Investor",
  "instrument_id": "TSLA",
  "instrument_name": "Tesla Shorting Losers Association",
  "trade_date_time": "2015-02-12T00:00:00",
  "trade_details": {
    "buySellIndicator": "BUY",
    "price": 7281273712,
    "quantity": 12
  },
  "trade_id": "177",
  "trader": "bob smith"
}

## searching non-existing trade 
### Request

`GET /search-trades/`

curl -X 'GET' \ 'http://localhost:8000/search-trades?search=bambiha' \ H 'accept: application/json' json' \
  
### Response

 content-length: 28 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:40:37 GMT 
 server: uvicorn
 {
  "detail": "trade not found"
    }

## filtering trades 
### Request

`GET /filter-trades/`

curl -X 'GET' \
  'http://localhost:8000/filter-trades?minPrice=100&maxPrice=1292390898.2487&start=2020-05-18T00%3A00%3A00&end=2020-05-18T00%3A00%3A00&asset_class=Stocks' \
  -H 'accept: application/json'  
### Response

 content-length: 302 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:48:06 GMT 
 server: uvicorn 

[
  {
    "asset_class": "Stocks",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-05-18T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 1292390898.2487,
      "quantity": 20
    },
    "trade_id": "1",
    "trader": "surjeet Rajput"
  }
]

## Pagination trades 
### Request

`GET /pagination/`

curl -X 'GET' \
  'http://localhost:8000/pagination?page=1&resultPerPage=4' \
  -H 'accept: application/json'
### Response
 content-length: 1180 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:51:29 GMT 
 server: uvicorn
[
  {
    "asset_class": "Stocks",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-05-18T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 1292390898.2487,
      "quantity": 20
    },
    "trade_id": "1",
    "trader": "surjeet Rajput"
  },
  {
    "asset_class": "Equities",
    "counterparty": "Individual Investor",
    "instrument_id": "AMZN",
    "instrument_name": "Amazon",
    "trade_date_time": "2022-01-08T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 9920898.287,
      "quantity": 10
    },
    "trade_id": "100",
    "trader": "Rajiv mahey"
  },
  {
    "asset_class": "Fixed Income",
    "counterparty": "Government",
    "instrument_id": "AAPL",
    "instrument_name": "American Association of Professional Landmen.",
    "trade_date_time": "2021-10-31T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 90772773.9,
      "quantity": 2
    },
    "trade_id": "12",
    "trader": "Nella Nirjalla"
  },
  {
    "asset_class": "Bonds",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-09-28T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 6389127389.27,
      "quantity": 4
    },
    "trade_id": "199",
    "trader": "Gautam Gangully"
  }
]

## sort trades as per trade_id 
### Request

`GET /sort-trades/`

curl -X 'GET' \
  'http://localhost:8000/sort-trades' \
  -H 'accept: application/json'
### Response
 content-length: 1722 
 content-type: application/json 
 date: Wed,29 Jun 2022 09:54:17 GMT 
 server: uvicorn 

[
  {
    "asset_class": "Stocks",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-05-18T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 1292390898.2487,
      "quantity": 20
    },
    "trade_id": "1",
    "trader": "surjeet Rajput"
  },
  {
    "asset_class": "Fixed Income",
    "counterparty": "Government",
    "instrument_id": "AAPL",
    "instrument_name": "American Association of Professional Landmen.",
    "trade_date_time": "2021-10-31T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 90772773.9,
      "quantity": 2
    },
    "trade_id": "12",
    "trader": "Nella Nirjalla"
  },
  {
    "asset_class": "Equities",
    "counterparty": "Individual Investor",
    "instrument_id": "AMZN",
    "instrument_name": "Amazon",
    "trade_date_time": "2022-01-08T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 9920898.287,
      "quantity": 10
    },
    "trade_id": "100",
    "trader": "Rajiv mahey"
  },
  {
    "asset_class": "Stocks",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2015-02-12T00:00:00",
    "trade_details": {
      "buySellIndicator": "BUY",
      "price": 7281273712,
      "quantity": 12
    },
    "trade_id": "177",
    "trader": "bob smith"
  },
  {
    "asset_class": "N/A",
    "counterparty": "N/A",
    "instrument_id": "AMZN",
    "instrument_name": "Amazon",
    "trade_date_time": "2005-04-12T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 7281272,
      "quantity": 9
    },
    "trade_id": "177",
    "trader": "Rana tunga"
  },
  {
    "asset_class": "Bonds",
    "counterparty": "Individual Investor",
    "instrument_id": "TSLA",
    "instrument_name": "Tesla Shorting Losers Association",
    "trade_date_time": "2020-09-28T00:00:00",
    "trade_details": {
      "buySellIndicator": "SELL",
      "price": 6389127389.27,
      "quantity": 4
    },
    "trade_id": "199",
    "trader": "Gautam Gangully"
  }
]
