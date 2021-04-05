import yfinance as stock 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

D1 = stock.download("AMZN", '2021-01-01')
D1.Close.plot(color="Orange")

D2 = stock.download("AAPL", '2021-01-01')
D2.Close.plot(color="Black")

D3 = stock.download("FB", '2021-01-01')
D3.Close.plot(color="Blue")

D4 = stock.download("IBM", '2021-01-01')
D4.Close.plot(color="Cyan")

D5 = stock.download("MSFT", '2021-01-01')
D5.Close.plot(color="Purple")

D6 = stock.download("SPOT", '2021-01-01')
D6.Close.plot(color="Green")

D7 = stock.download("TSLA", '2021-01-01')
D7.Close.plot(color="Red")

plt.title("Stock Market Activity",
          fontsize = 40)
plt.legend(["Amazon", "Apple", "Facebook", "IBM", "Microsoft", "Spotify", "Tesla"])
plt.style.use(['dark_background'])
plt.show()