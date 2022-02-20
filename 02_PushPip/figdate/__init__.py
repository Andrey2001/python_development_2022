#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""Current date in the form of pyfiglet."""

import pyfiglet
import sys
from time import gmtime, strftime
import locale
from optparse import OptionParser


locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

def date(format="%Y %d %b, %A", font = "graceful"):
    """
    returns beautiful current date
    """
    date = strftime(format, gmtime())
    pyfiglet.print_figlet(date, font=font)

__all__ = ["date"]
__author__ = 'Kazarinov Andrey, kazarandrey@yandex.ru'

def main():
    parser = OptionParser(usage='%prog [options]')
    parser.add_option('--format', default="%Y %d %b, %A", 
                      help='date format (corresponds time.strftime())',
                      metavar='FORMAT')
    parser.add_option('--font', default="graceful",
                      help='font to render (default: %default)',
                      metavar='FONT')
    opts, args = parser.parse_args()
    if opts.format and opts.font: # all options
        date(opts.format, opts.font)
        exit(0)
    if opts.format: # only format options
        date(opts.font)
        exit(0)
    parser.print_help()
    return 1

if __name__ == '__main__':
    sys.exit(main())