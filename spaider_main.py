import url_manager
import html_download
import html_parser
import html_outputer
import os

class Spaidermain(object):

    def __init__(self):
        self.urls = url_manager.urlManager()
        self.download = html_download.htmlDownload()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.HtmlOutputer()
        

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        #self.urls.get_new_url()
        while self.urls.has_new_url():
            try:
                
                new_url = self.urls.get_new_url()
                print "craw %d : %s" %(count, new_url)
                html_cont = self.download.Download(new_url)
                
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count + 1
                if count == 10:
                    break
            except:
                print "craw fail"
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/4566.htm"
    spaider = Spaidermain()
    spaider.craw(root_url)










