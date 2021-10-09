# Python-Assignment2-Abylaikhan-A

## Title: Providing lates information and news of specific crypto currency using requests (Dynamic scrapping)

## Installation
To be able to use the programm you should install ```requests_html``` library

## Usage 
1. Create coin object in order to get all neccessary  information of specific cryptocurrency
```coin = Coin(<name of a coin>)```
1. Getting recent crypto news on particular coin
```coin.get_news()```
1. Getting information of the coin
```coin.get_info()```

## Usage Examples 
* creating coin object (bitcoin) ```btc = Coin('bitcoin')```
* getting crypto news on particular coin (bitcoin) ```btc.get_news()```
* getting information on the same coin (bitcoin) ```btc.get_info()```

* creating coin object (etherium) ```eth = Coin('ethertium')```
* getting crypto news on particular coin (etherium) ```eth.get_news()```
* getting information on the same coin (etherium) ```eth.get_info()```
