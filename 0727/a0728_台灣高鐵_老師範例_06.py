import twstock

stock = twstock.Stock('2012')
print("近3個月的收盤價")
print(stock.price) #近31個收盤價
print("近6天收盤價")
print(stock.price[-6:])

rel=twstock.realtime.get('2012')
if rel['success']:
    print('股票即時資料')
    print(rel)
else:
    print('錯誤:'+rel['rtmessage'])

print("目前股價")
print(rel['realtime']['latest_trade_price'])

