#coding:utf8
import zhanzhang_dict_pc,zhanzhang_dict_mobile,zhanzhang_dict_pc_360,zhanzhang_dict_mobile_360
def zhanzhang(url):
    print "\n【开始抓取百度PC关键词】\n"
    zhanzhang_dict_pc.get_pc_keywords(url)   #百度PC
    print "\n【开始抓取百度移动关键词】\n"
    zhanzhang_dict_mobile.get_m_keywords(url)  #百度移动
    print "\n【开始抓取360PC关键词】\n"
    zhanzhang_dict_pc_360.get_pc_keywords_360(url)   #360PC
    print "\n【开始抓取360移动关键词】\n"
    zhanzhang_dict_mobile_360.get_mobile_keywords_360(url)   #360移动

    print "\n抓取结束!\n"

if __name__=="__main__":
    # url="xhj.com"
    # url="lianjia.com"
    # url="fang.com"

    #url="loupan.com"
    # url="qfang.com"
    url="jiwu.com/"
    url="julive.com"
    zhanzhang(url)
