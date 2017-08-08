#!/usr/bin/env python

import webbrowser

def launch(*args):
    """Launches the Yahoo Finanace pages for the tickers specified by *args.

    Arguments:
    *args -- A variable-length iterable of tickers.
    """
    if args:
        for symbol in args:
            url = 'https://finance.yahoo.com/quote/{0}?p={0}'.format(symbol)
            webbrowser.open_new_tab(url)

if __name__ == '__main__':
    launch('^GSPC')
