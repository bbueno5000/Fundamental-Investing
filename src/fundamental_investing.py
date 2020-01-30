import matplotlib.dates as mpl_dates
import matplotlib.pyplot as pyplot
import numpy
import urllib.request

show_charts = input('Would you like to show the financial data (Quandl) charts? (Y/N): ')

if show_charts.lower()=='y':
    print('okay, charts will be shown')
elif show_charts.lwoer()=='n':
    print('okay, charts will NOT be shown.')
else:
    print('invalid input, charts will NOT be shown.')

def grab_quandl(ticker_symbol):
    net_income_array = []
    revenue_array = []
    return_on_capital_array = []
    end_link = 'sort_order=asc'
    try:
        net_income = urllib.request.urlopen(
            'http://www.quandl.com/api/v1/datasets/OFDP/DMDRN_' 
            + ticker_symbol.upper() 
            + '_NET_INC.csv?&' + end_link
            ).read()
        revenue = urllib.request.urlopen(
            'http://www.quandl.com/api/v1/datasets/OFDP/DMDRN_' 
            + ticker_symbol.upper() 
            + '_REV_LAST.csv?&' + end_link
            ).read()
        return_on_capital = urllib.request.urlopen(
            'http://www.quandl.com/api/v1/datasets/OFDP/DMDRN_' 
            + ticker_symbol.upper() 
            + '_ROC.csv?&' + end_link
            ).read()
        split_net_income = net_income.split('\n')
        print('Net Income:')
        for each_net_income in split_net_income[1:-1]:
            print(each_net_income)
            net_income_array.append(each_net_income)
        print('___________')
        split_revenue = revenue.split('\n')
        print('Revenue:')
        for each_revenue in split_revenue[1:-1]:
            print(each_revenue)
            revenue_array.append(each_revenue)
        print('___________')
        split_return_on_capital = return_on_capital.split('\n')
        print('Return On Capital:')
        for each_return_on_capital in split_return_on_capital[1:-1]:
            print(each_return_on_capital)
            return_on_capital_array.append(each_return_on_capital)
        income_date, income = numpy.loadtxt(
            net_income_array, 
            delimiter=',', 
            unpack=True,
            converters={0: mpl_dates.strpdate2num('%Y-%m-%d')}
            )
        revenue_date, revenue = numpy.loadtxt(
            revenue_array, 
            delimiter=',',
            unpack=True, 
            converters={0: mpl_dates.strpdate2num('%Y-%m-%d')}
            )
        return_on_capital_date, return_on_capital = numpy.loadtxt(
            return_on_capital_array, 
            delimiter=',',
            unpack=True,
            converters={0: mpl_dates.strpdate2num('%Y-%m-%d')}
            )
        #axis_1 = pyplot.subplot2grid((6,6), (0,0), rowspan=2, colspan=6)
        #axis_1.plot(income_date, income)
        #pyplot.ylabel('Net Income')
        #axis_2 = pyplot.subplot2grid((6,6), (2,0), sharex=axis_1, rowspan=2, colspan=6)
        #axis_2.plot(revenue_date, revenue)
        #pyplot.ylabel('Revenue')
        #axis_3 = pyplot.subplot2grid((6,6), (4,0), sharex=axis_1, rowspan=2, colspan=6)
        #axis_3.plot(return_on_capital_date, return_on_capital)
        #pyplot.ylabel('ROC')
        #axis_1.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d'))
        #pyplot.subplots_adjust(hspace=0.53)
        #pyplot.suptitle(ticker_symbol)
        #pyplot.show()
    except Exception as exception:
        print('failed the main quandl loop:', str(exception))
    return revenue_date, revenue, return_on_capital_date, return_on_capital, income_date, income

def key_statistics(stock):
    """
    Definitions:
        pbr - price to book ratio
        pe12t - trailing price/earnings (12 months)
        peg5 - price/earnings to growth ratio (5 years expected)
    """
    try:
        source_code = urllib.request.urlopen('http://finance.yahoo.com' + stock).read()
        pbr = source_code.split('Price/Book')[1].split('</td>')[0]
        if float(pbr) < 1:
            peg5 = source_code.split(
                'PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">'
                )[1].split('</td>')[0]
            if 0 < float(peg5) < 2:
                debt_equity_ratio = source_code.split(
                    'Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">'
                    )[1].split('</td>')[0]
                pe12t = source_code.split(
                    'Trailing P/E (ttm, intraday):</td><td class="yfnc_tabledata1">'
                    )[1].split('</td>')[0]
                if float(pe12t) < 15:
                    print('______________________________________')
                    print('')
                    print(stock, 'meets requirements')
                    print('price to book:', pbr)
                    print('PEG forward 5 years', peg5)
                    print('Trailing PE (12mo):',pe12t)
                    print('Debt to Equity:', debt_equity_ratio)
                    print('______________________________________')
                    if show_charts.lower() == 'y':
                        grab_quandl(stock)
    except Exception as exception:
        print('error:main loop:', str(exception))

def parse_russell():
    ticker_symbols = []		
    try:
        read_file = open('data/russell3000.txt','r').read()
        split_file = read_file.split('\n')
        for line in split_file:
            split_line = line.split(' ')
            ticker_symbol = split_line[-1]
            ticker_symbols.append(ticker_symbol)
            print(ticker_symbols)
    except Exception:
        pass

if __name__ == '__main__':
    #for stock in sp500short:
    #    key_statistics(stock)
    #    time.sleep(1)
    #parse_russell()
    grab_quandl('YHOO')
