#coding:utf8
#站长工具PC关键词收集（只提取有指数且有排名关键词）  使用方法，输入某网站网址，即可提取网站所有有排名关键词数据并自动导入数据库
import requests,re,time,MySQLdb,time
conn=MySQLdb.connect(host="localhost",user="root",passwd='',db="fang_dict" ,port=3306,charset="utf8")  #连接数据库
cursor=conn.cursor()  #定位一个指针
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0"}
def GetHtml(url):
    urlNew="http://rank.chinaz.com/?host=%s&st=0&c=&sortType=0&page=1"%url   #关键词权重查询页面URL
    while 1:
        try:
            html=requests.get(urlNew,header).text
            return html
        except:
            pass
def get_pc_keywords(url):
    html=GetHtml(url)
    if u'条记录' in html:
        if u'暂无数据' not in html:
            Keywords_num=re.findall('<i class="col-blue02">(\d+)</i>',html)[0]  #共有多少条记录
            nums=int(Keywords_num)/20+2    #算出总页数
            for num in range(1,nums):  #循环打开每一页
                url_num="http://rank.chinaz.com/?host=%s&st=0&c=&sortType=0&page=%s"%(url,num)
                try:
                    html=requests.get(url_num).text
                    keywords=re.findall('ellipsis block">([\s\S]*?)</a><div class=',html)
                    if keywords:
                        indexs=re.findall('<a href="http://index.chinaz.com/\?words=[\s\S]*?#.*?-module" target="_blank">(\d+)</a></div><div class="w8-0">',html)
                        for x  in range(0,len(keywords)):
                            # print '关键词：',keywords[x],'整体指数：',indexs[x*3],'PC指数：',indexs[x*3+1],'移动指数：',indexs[x*3+2]
                            try:
                                cursor.execute("insert into fangdict(word,total_index,pc_index,m_index) VALUES ('%s',%s,%s,%s)"%(keywords[x],indexs[x*3],indexs[x*3+1],indexs[x*3+2]))
                                print url,'[百度PC]关键词：',keywords[x],'---已成功添加到数据库----'
                                time.sleep(10)
                                conn.commit()
                            except:
                                print url,'[百度PC]关键词：',keywords[x],'*******在数据库中已存在********'
                                continue

                    else:
                        pass
                except:
                    pass
        else:
            pass
    else:
        print '【百度PC，第一页关键词数不超过20条】\n'

        keywords=re.findall('ellipsis block">([\s\S]*?)</a><div class=',html)
        if keywords:
            indexs=re.findall('<a href="http://index.chinaz.com/\?words=[\s\S]*?#.*?-module" target="_blank">(\d+)</a></div><div class="w8-0">',html)
            for x  in range(0,len(keywords)):
                # print '关键词：',keywords[x],'整体指数：',indexs[x*3],'PC指数：',indexs[x*3+1],'移动指数：',indexs[x*3+2]
                try:
                    cursor.execute("insert into fangdict(word,total_index,pc_index,m_index) VALUES ('%s',%s,%s,%s)"%(keywords[x],indexs[x*3],indexs[x*3+1],indexs[x*3+2]))
                    print url,'[百度PC]关键词：',keywords[x],'---已成功添加到数据库----'
                    time.sleep(10)
                    conn.commit()
                except:
                    print url,'[百度PC]关键词：',keywords[x],'*******在数据库中已存在********'
                    continue

        else:
            pass

if __name__=="__main__":

    url="zz.xhj.com"
    get_pc_keywords(url)
