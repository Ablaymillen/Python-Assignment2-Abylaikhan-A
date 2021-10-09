import sys
sys.path.append('src/src.py')
from src.src import Coin

# creating coin object (bitcoin)
btc = Coin('bitcoin')

# getting crypto news on particular coin (bitcoin)
btc.get_news()

# getting information on the same coin (bitcoin)
btc.get_info()
