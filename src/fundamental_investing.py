
import time
import urllib

sp500short = [
    'a', 
    'aa', 
    'aapl', 
    'abbv', 
    'abc', 
    'abt', 
    'ace', 
    'aci', 
    'acn', 
    'act', 
    'adbe', 
    'adi', 
    'adm', 
    'adp'
    ]

def key_statistics(stock):
    """
    Definitions:
        pbr - price to book ratio
    """
    try:
        source_code = urllib.urlopen('http://finance.yahoo.com' + stock).read()
        pbr = source_code.split('Price/Book')[1].split('</td>')[0]
        if float(pbr) < 0.70:
            print('Price/Book:', pbr)
    except Exception as e:
        print('error:main loop:', stock, str(e))

if __name__ == '__main__':
    for stock in sp500short:
        key_statistics(stock)
        time.sleep(1)
