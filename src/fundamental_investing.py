
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
    'adp',
    'rsh'
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
            print('Price/Book:', stock, pbr)
            peg5 = source_code.split(
                'PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">'
                )[1].split('</td>')[0]
            if 0 < float(peg5) < 1:
                print(stock, 'meets requirements')
                print(pbr)
                print(peg5)
    except Exception as e:
        print('error:main loop:', str(e))

if __name__ == '__main__':
    for stock in sp500short:
        key_statistics(stock)
        time.sleep(1)
