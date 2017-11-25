from bs4 import BeautifulSoup
import urllib.parse
import re

class HtmlParser(object):
#https://baike.baidu.com/item/Python/407313
    def _get_new_urls(self,page_url,soup):#获取页面中其他词条的url
        new_urls=set()#将新的url存入一个列表里
        links=soup.find_all('a',href=re.compile(r'/item'))
        for link in links:
            new_url=link['href']
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

#<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
    def _get_new_data(self, page_url, soup):
       #解析title和summa的数据
        res_data={}
        res_data['url']=page_url
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find('div',class_='lemma-summary')
        res_data['summary']=summary_node.get_text()
        return res_data




    def Parser(self,page_url,html_cont):#解析出url列表和数据
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return  new_urls,new_data

