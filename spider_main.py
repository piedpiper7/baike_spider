from baike_spider import url_manager,html_download,html_parser,html_output


class SpiderMain(object):

    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.download=html_download.HtmlDownload()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_output.HtmlOutput()
#在构造函数中初始化使用的对象

    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)#将入口url加入url管理器
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()#获取待爬取的url
                print('crow %s:%s'%(count,new_url))
                html_cont=self.download.Download(new_url)#用下载器下载页面，并存储
                new_urls,new_data=self.parser.Parser(new_url,html_cont)#用解析器解析页面，获取新的url和数据
                self.urls.add_new_urls(new_urls)#补充新的url到url管理器
                self.outputer.collect_data(new_data)#数据收集
                if count==50:
                    break
                count=count+1
            except:
                print('crow filed!')
        self.outputer.output_html()


if __name__=='__main__':
    root_url='https://baike.baidu.com/item/Python/407313'#入口url
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)#启动爬虫