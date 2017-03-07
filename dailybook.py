#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 07/03/2017

@author: julio77nz
'''

import urllib2
import bs4

class Client(object):

    """Web Client, for www.udl.Created

    Downloads www.udl.cat main page to parse
    for agenda items"""

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def parse_web_page(self, html):
        """
        Parses an html page searching for the agenda
        """
        soup = bs4.BeautifulSoup(html)
        dailybook = soup.find_all("div", "dotd-title")
        return dailybook

    def run(self):
        """
        Retrieves the book from https://www.packtpub.com/ and print it
        """
        html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning/")
        dailybook = self.parse_web_page(html)
        print(dailybook)


if __name__ == "__main__":
    client = Client()
    client.run()
