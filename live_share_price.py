import requests
import urllib2,urllib
import json
import time
import os

class live_share_price:
    def __init__(self):
        import ConfigParser
        # Authentication details. To  obtain these visit dev.twitter.com
        config = ConfigParser.ConfigParser()
        config.read('C:/PyStockTicker/stock.conf')
        self.company_list = config.get('stock_details', 'company_list').split(";")
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    def get_value(self,identifier):
        wiki =  self.prefix + identifier
        # Query the website and return the data and parse the xml using untangle
        page = urllib2.urlopen(wiki)
        data = page.read()
        obj = json.loads(data[3:])
        #print obj[0]
        return obj[0]["l_cur"]+"~"+obj[0]["c"]+"~"+obj[0]["cp"]

    def print_list_report(self,rpt_name,rpt_data,hdr_data):
        try:
            HTMLFILE = 'C:/PyStockTicker/' + rpt_name + '.html'
            f = open(HTMLFILE, 'w')
            f.write('<html><body><h1>')
            f.write(rpt_name + " Report ")
            f.write('</h1>')
            f.write('<table border = "1">')
            f.write('<tr>')
            for head in hdr_data:
                f.write('<th>')
                f.write(head)
                f.write('</th>')
            f.write('</tr>')
            for data in rpt_data:
                f.write(data)
        except Exception, e1:
            print str(e1)

if __name__ == "__main__":
    lsp = live_share_price()
    rpt_data=[]
    header = ['STOCK','CMP','Change','Change %']
    company_list = lsp.company_list;
    for company in company_list:
        data = lsp.get_value(company).split("~")
        rpt_data.append("<tr><td>" + company +
                         "</td><td>" + str(data[0]) +
                        "</td><td>" + str(data[1]) +
                        "</td><td>" + str(data[2]) +
                        "</tr>")
        #print company + ':' + share_value
    lsp.print_list_report('share_price',rpt_data,header)
