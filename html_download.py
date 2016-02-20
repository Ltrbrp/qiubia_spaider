from bs4 import BeautifulSoup
import urllib2


class htmlDownload(object):
    
    def Download(self, url):
        if url is None:
            return

        reponse = urllib2.urlopen(url)
        if reponse.getcode() != 200:
            return
        return reponse.read()