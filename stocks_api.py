import alpaca_trade_api as tradeapi
from alpaca_trade_api import StreamConn

investment = input("What position do you wanna invest in?: ")
##if investment == "nah" or investment == "cancelling":
  ##  print("Well ok then")

class Martingale(object):
    def __init__(self):
        self.key = 'PKBN616SDCWH35HYX79J'
        self.secret = 'UgTar1USmbor29nBAMjXMkJJB26XxB9cHUlechUY'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)
        self.symbol = investment
        self.current_order = None
        self.last_price = 1

        try:
            self.position = int(self.api.get.position(self.symbol).qty)
        except:
            self.position = 0

    def submit_order(self, target):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)

        delta = target - self.position
        if delta == 0:
            return
        print(f"Processing the order for {target} shares.")

        if delta > 0:
            buy_shares = delta
            if self.position < 0:
                buy_shares = min(abs(self.position), buy_shares)
            print(f"Buying {buy_shares} shares.")
            self.current_order = self.api.submit_order(self.symbol, buy_shares, 'buy', 'limit', 'day', self.last_price)

        elif delta < 0:
            sell_shares = abs(delta)
            if self.position > 0:
                sell_shares = miqn(abs(self.position), sell_shares)
            print(f"Selling {sell.shares} shares.")
            self.current_order = self.api.submit_order(self.symbol,sell_shares,'sell','limit','day', self.last_price)

            self.cancel_order = close
            

if __name__ == '__main__':
    t = Martingale()
    t.submit_order(1) ## 1 share order = 1 buck (referring to any unit of currency)


##In case you're wondering if you stumble upon this project. The first 5 investments were just experimental tests. That is why I decided to buy 3 shares of apple lmao.
