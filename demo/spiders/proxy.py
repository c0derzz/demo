# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import threading
import telnetlib

#初始换浏览器header
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

def get_ip():
    #获取代理ip 返回列表数据
    httpResult=[]
    httpsResult=[]
    IPBaseUrl = "https://www.kuaidaili.com/ops/proxylist/"
    print("-------in------")
    try:
        for page in range(1,10):
            IPPageUrl = IPBaseUrl + str(page)
            IPResp = requests.get(IPPageUrl,headers=headers)
            IPText = IPResp.text
            soupIP = BeautifulSoup(IPText,"lxml")
            freeListDiv = soupIP.find('div',id='freelist')
            IPTrs = freeListDiv.find_all('tr')
            for IPTr in IPTrs[1:]:
                tds = IPTr.find_all('td')
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                protocols = tds[3].text.strip().split(',')
                for p in protocols:
                    if p.strip() == 'HTTP':
                        httpResult.append('http://' + ip + ':' + port)
                    elif p.strip() == 'HTTPS':
                        httpsResult.append('https://' + ip + ':' + port)
                    else:
                        print("非法的协议：",p)

    except BaseException as e:
        print("exception:",e)
    return httpResult,httpsResult
#验证ip地址的可用性 可用telnetlib模块进行校验
def check_http(ip,pt):
    f = open("D:\work-self\scrapy-demo\demo\demo\data\ip_http.txt","a")
    f.truncate()
    try:
        telnetlib.Telnet(ip,port=pt,timeout=5)
    except:
        print("fail:",ip+":"+pt)
    else:
        print("success:", ip + ":" + pt)
        f.write(ip+":"+pt+"\n")

# 验证ip地址的可用性 可用telnetlib模块进行校验
def check_https(ip,pt):
    f = open("D:\work-self\scrapy-demo\demo\demo\data\ip_https.txt","a")
    f.truncate()
    try:
        telnetlib.Telnet(ip,port=pt,timeout=5)
    except:
        print("fail:",ip+":"+pt)
    else:
        f.write(ip+":"+pt+"\n")

#使用代理访问网站 来验证是否可用
def check_by_net(pro,ip,pt):
    url=''
    if pro.strip() == 'HTTP':
        url=ip + ':' + pt
    elif pro.strip() == 'HTTPS':
        url = ip + ':' + pt
    else:
        print("非法的协议：", pro)
    try:
        print("proxy url:",url)
        requests.get("https://www.autohome.com.cn/beijing/",headers=headers,proxies={'http':url},timeout=3)
    except BaseException as e:
        print("出现异常：",e)
    else:
        print('---------------------------success:',url)

def main():
    httpResult,httpsResult=get_ip()
    print("http size is :",len(httpResult))
    print("https size is :",len(httpsResult))
    if len(httpResult) == 0 and len(httpsResult) == 0:
        print("没有可执行数据")
        pass

    #循环执行http数据 telnet判断有效性
    if len(httpResult) > 0:
        threads = []
        open("D:\spider-workspace\demo\demo\data\ip_http.txt", "a").truncate()
        for i in httpResult:
            ip = str(i.split(":")[-2][2:].strip())
            pt = str(i.split(":")[-1].strip())
            #t = threading.Thread(target=check_by_net, args=('HTTP',ip, pt))
            t = threading.Thread(target=check_http, args=(ip, pt))
            threads.append(t)
        for i in range(len(httpResult)):
            threads[i].start()

        for i in range(len(httpResult)):
            threads[i].join()

    #循环https 数据
    if len(httpsResult) > 0:
        threads_https = []
        open("D:\spider-workspace\demo\demo\data\ip_https.txt", "a").truncate()
        for i in httpsResult:
            ip = str(i.split(":")[-2][2:].strip())
            pt = str(i.split(":")[-1].strip())
            t = threading.Thread(target=check_https, args=(ip, pt))
            threads_https.append(t)

        for i in range(len(httpsResult)):
            threads_https[i].start()

        for i in range(len(httpsResult)):
            threads_https[i].join()


if __name__ == '__main__':
    main()
