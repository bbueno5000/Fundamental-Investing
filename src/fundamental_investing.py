
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
        de - debt/equity
        pbr - price to book ratio
        pe12t - trailing price/earnings (12 months)
        peg5 - price/earnings to growth ratio (5 years expected)
    """
    try:
        source_code = urllib.urlopen('http://finance.yahoo.com' + stock).read()
        pbr = source_code.split('Price/Book')[1].split('</td>')[0]
        if float(pbr) < 1:
            peg5 = source_code.split(
                'PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">'
                )[1].split('</td>')[0]
            if 0 < float(peg5) < 1:
                de = source_code.split(
                    'Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">'
                    )[1].split('</td>')[0]
                pe12t = sourceCode.split(
                    'Trailing P/E (ttm, intraday):</td><td class="yfnc_tabledata1">'
                    )[1].split('</td>')[0]
                if float(PE12) < 15:
                    print('______________________________________')
                    print('')
                    print(stock, 'meets requirements')
                    print('price to book:', pbr)
                    print('PEG forward 5 years', peg5)
                    print('Trailing PE (12mo):',pe12t)
                    print('Debt to Equity:', de)
                    print('______________________________________')
    except Exception as e:
        print('error:main loop:', str(e))

def parse_russell():
    tickers = []		
    try:
        read_file = open('data/russell3000.txt','r').read()
        split_file = read_file.split('\n')
        for line in split_file:
            split_line = line.split(' ')
            ticker = split_line[-1]
            tickers.append(ticker)
            print(tickers)
    except Exception as e:
        pass

if __name__ == '__main__':
    for stock in sp500short:
        key_statistics(stock)
        time.sleep(1)
    parse_russell()
