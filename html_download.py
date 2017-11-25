import urllib.request

class HtmlDownload(object):

    def Download(self,url):#网页下载器
        if url is None:
            return
        response=urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()