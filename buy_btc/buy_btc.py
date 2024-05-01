from binance.client import Client
from binance.enums import *
from youtube.buy_btc.secrets import api_key, api_secret

client = Client(api_key, api_secret)

# try:
#     order = client.create_order(
#         symbol='BTCUSDT',
#         side=SIDE_BUY,
#         type=ORDER_TYPE_MARKET,
#         quantity=0.0001,
#     )
#
#     print(order)
# except Exception as e:
#     print("Erro ao criar ordem",e)


print(client.get_my_trades(symbol='BTCUSDT'))