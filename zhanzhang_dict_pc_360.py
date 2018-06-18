#coding:utf8
#站长工具360PC关键词收录（只提取有指数且有排名关键词）  使用方法，输入某网站网址，即可提取网站所有有排名关键词数据并自动导入数据库
import requests,re,time,MySQLdb,time,urllib,urllib2,sys
conn=MySQLdb.connect(host="localhost",user="root",passwd='',db="fang_dict" ,port=3306,charset="utf8")  #连接数据库
cursor=conn.cursor()  #定位一个指针
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"}
# post_data={"sortType":"0","host":"xhj.com"}
# post_data=urllib.urlencode(post_data)
def GetHtml(url):
    post_data={"sortType":"0","host":"%s"%url}
    post_data=urllib.urlencode(post_data)
    urlNew="http://rank.chinaz.com/sorank/%s-0---0-1"%url   #关键词权重查询页面URL
    req=urllib2.Request(url=urlNew,data=post_data,headers=header)
    html=urllib2.urlopen(req).read()
    return html
def get_pc_keywords_360(url):
    post_data={"sortType":"0","host":"%s"%url}
    post_data=urllib.urlencode(post_data)
    html=GetHtml(url)
    if '条记录' in html:
        if 'col-red lh30 fz14 tc' not in html:
            Keywords_num=re.findall('<i class="col-blue02">(\d+)</i>',html)[0]  #共有多少条记录
            nums=int(Keywords_num)/20+2    #算出总页数,故意多算一个，方面下面循环
            for page in range(1,nums):  #循环打开每一页
                url_num='http://rank.chinaz.com/sorank/%s-0---0-%s'%(url,page)
                if page<=1:
                    try:
                        req=urllib2.Request(url=url_num,data=post_data,headers=header)
                        html=urllib2.urlopen(req).read()
                        keywords=re.findall('ellipsis block">([\s\S]*?)</a></div><div class="w14-0',html)
                        if keywords:
                            indexs=re.findall('<a href="http://index.chinaz.com/\?words=[\s\S]*?#haosou-module" target="_blank">(\d+)</a></div><div class="w13-0',html)
                            for x  in range(0,len(keywords)):
                                # print '关键词：',keywords[x],'360指数：',indexs[x]
                                try:
                                    cursor.execute("insert into fangdict(word,360_pc_index) VALUES ('%s',%s)"%(keywords[x],indexs[x]))
                                    print url,'[360pc]关键词：',keywords[x],'---已成功添加到数据库----'
                                    time.sleep(10)
                                    conn.commit()
                                except:
                                    print url,'[360pc]关键词：',keywords[x],'*******在数据库中已存在********'
                                    continue

                        else:
                            pass
                    except:
                        print '打开分页网址有误，检查网络是否正常'

                else:
                    try:
                        html=requests.get(url_num).content
                        keywords=re.findall('ellipsis block">([\s\S]*?)</a></div><div class="w14-0',html)
                        if keywords:
                            indexs=re.findall('<a href="http://index.chinaz.com/\?words=[\s\S]*?#haosou-module" target="_blank">(\d+)</a></div><div class="w13-0',html)
                            for x  in range(0,len(keywords)):
                                # print '关键词：',keywords[x],'360PC指数：',indexs[x]
                                try:
                                    cursor.execute("insert into fangdict(word,360_pc_index) VALUES ('%s',%s)"%(keywords[x],indexs[x]))
                                    print url,'[360PC]关键词：',keywords[x],'---已成功添加到数据库----'
                                    time.sleep(10)
                                    conn.commit()
                                except:
                                    print url,'[360pc]关键词：',keywords[x],'*******在数据库中已存在********'
                                    continue

                        else:
                            pass

                    except:
                        pass

        else:
            pass
    else:

        print '【360PC，第一页关键词数不超过20条】\n'
        keywords=re.findall('ellipsis block">([\s\S]*?)</a></div><div class="w14-0',html)
        if keywords:
            indexs=re.findall('<a href="http://index.chinaz.com/\?words=[\s\S]*?#haosou-module" target="_blank">(\d+)</a></div><div class="w13-0',html)
            for x  in range(0,len(keywords)):
                # print '关键词：',keywords[x],'360PC指数：',indexs[x]
                try:
                    cursor.execute("insert into fangdict(word,360_pc_index) VALUES ('%s',%s)"%(keywords[x],indexs[x]))
                    print url,'[360PC]关键词：',keywords[x],'---已成功添加到数据库----'
                    time.sleep(10)
                    conn.commit()
                except:
                    print url,'[360pc]关键词：',keywords[x],'*******在数据库中已存在********'
                    continue

        else:
            pass

if __name__=="__main__":
    url="xhj.com"
    get_pc_keywords_360(url)
