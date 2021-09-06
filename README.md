# Bitcoin-price-alert

## Introduction
This application will display an alert whenever the price of you favourite cryptocurreny changes abruptly.

## Installation
Python 3.8+ is recommended, but it might work on previous versions as well. `pipenv` is required for installing dependencies.

* Install pipenv on your machine:

```sh
pip install pipenv
```

* Install the remaining dependencies:

```sh
pip install pipfile
```

* Run the file:

```sh
python -m fetchPrice.py
```

## Usage
Add the name of the currency to the list `currencies` you want to follow. For example, to follow Bitcoin and Ethereum prices, do this:
```
currencies = [
    'BTC',
    'ETH'
]
```

## Licence
MIT
