#coding:utf8
#获取任意网页源代码
import requests,re
headers={"User-Agent":"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）"}
def get_html(url):
    html1=requests.get(url,headers=headers).content
    if 'gb2312' in html1 or 'GB2312' in html1:
        r=requests.get(url,headers=headers)
        r.encoding='gb2312'
        html=r.text
        return html
    elif 'gbk' in html1 or 'GBK' in html1:
        r=requests.get(url,headers=headers)
        r.encoding='gbk'
        html=r.text
        return html
    else:
        html=html1
        return html
if __name__=="__main__":
    url="http://www.baidu.com"
    get_html(url)
