# This is the DSS Format in JSON

## This is for the price action of a share over 7 days
```json
{
  "metadata": {
    "description": "The price of a share over 7 days"
    "accuracy_formula": "",
  },
  "features": {
    "X": ["timestamp","price"],
    "Y": ["next_price"]
  },
  "data": {
    0: {
      "timestamp": "07-01-2023",
      "price": 100.23,
      "next_price": 105.30
    },
    1: {
      "timestamp": "07-02-2023",
      "price": 105.30,
      "next_price": 103.41
    },
    2: {
      "timestamp": "07-03-2023",
      "price": 103.41,
      "next_price": 102.23
    },
    3: {
      "timestamp": "07-04-2023",
      "price": 102.23,
      "next_price": 110.11
    },
    4: {
      "timestamp": "07-05-2023",
      "price": 110.11,
      "next_price": 96.04
    },
    5: {
      "timestamp": "07-06-2023",
      "price": 96.04,
      "next_price": 105.23
    },
    6: {
      "timestamp": "07-07-2023",
      "price": 105.23,
      "next_price": 105.23
    },
  },
}
```
## This is for a more complex data set with multiple features
```json
{
  "metadata": {
    "description": "The the open, high, low, close of a share over 7 days"
    "accuracy_formula": "",
  },
  "features": {
    "X": ["timestamp", "open"],
    "Y": ["high", "low", close"]
  }.
  "raw_data": {
    0: {
      "timestamp": "07-01-2023",
      "open": 100.23,
      "high": 101.25,
      "low": 99.48,
      "close": 100.48
    },
    1: {
      "timestamp": "07-02-2023",
      "open": 105.30,
      "high": 108.43,
      "low": 103.30,
      "close": 104.40
    },
    2: {
      "timestamp": "07-03-2023",
      "open": 103.41,
      "high": 105.33,
      "low": 101.86,
      "close": 103.25
    },
    3: {
      "timestamp": "07-04-2023",
      "open": 102.23,
      "high": 102.24,
      "low": 98.56,
      "close": 100.33
    },
    4: {
      "timestamp": "07-05-2023",
      "open": 110.11,
      "high": 122.32,
      "low": 102.77,
      "close": 115.31
    },
    5: {
      "timestamp": "07-06-2023",
      "open": 96.04,
      "high": 98.03,
      "low": 90.13,
      "close": 95.44
    },
    6: {
      "timestamp": "07-07-2023",
      "open": 105.23,
      "high": 110.56,
      "low": 103.33,
      "close": 106.78
    },
  },
}
```
