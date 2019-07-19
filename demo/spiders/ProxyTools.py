'''
@File : ProxyTools.py
@Author : liruichuan
@Date: 2019/7/19
@Desc:
'''

import requests
import threading
import re
from queue import Queue
import telnetlib
import logging
from bs4 import BeautifulSoup

# 公共请求headers信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

'''
获取快代理网站免费的代理ip列表
'''


def get_kuaidaili_proxy_list():
    base_host = "https://www.kuaidaili.com/ops/proxylist/"
    # http 代理结果
    http_proxy_list = []
    # https 代理结果
    https_proxy_list = []
    try:
        for pageNo in range(1, 10):
            resp = requests.get(base_host + str(pageNo), headers=headers)
            if resp.status_code != 200:
                continue
            kdl_soup = BeautifulSoup(resp.text, 'lxml')
            trs = kdl_soup.find('div', id='freelist').find_all('tr')
            for tr in trs[1:]:
                tds = tr.find_all('td')
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                protocols = tds[3].text.strip().split(',')

                if protocols[0] is not None and protocols[0].strip() == 'HTTP':
                    http_proxy_list.append('http://' + ip + ':' + port)
                if len(protocols) > 1 and protocols[1] is not None and protocols[1].strip() == 'HTTPS':
                    https_proxy_list.append('https://' + ip + ':' + port)
    except Exception as e:
        logging.error("发生异常：", exc_info=True)
    return http_proxy_list, https_proxy_list


def check_save_proxy(path='', data=[]):
    """
    :param path: 文件路径
    :param data: 需要验证数据
    """
    if path and data:
        threads = []
        backValue = Queue()
        f = open(path, 'a')
        f.truncate()
        #http_pattern = re.compile(r'http?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
        #https_pattern = re.compile(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
        for d in data:
            #http = re.match(http_pattern, d)
            #https = re.match(https_pattern, d)
            try:
                ip = str(d.split(":")[-2][2:].strip())
                pt = str(d.split(":")[-1].strip())
                t = threading.Thread(target=do_check, args=(ip, pt, backValue))
                t.start()
                threads.append(t)
            except Exception as ex:
                print("异常信息：%s" % ex)
                print("telnet fail:", ip + ":" + pt)
        for i in range(len(data)):
            threads[i].join()
        print("执行成功")
        for _ in range(len(data)):
            success_ip=backValue.get()
            print("成功ip:", success_ip)
            f.write(success_ip+"\n")
    raise Exception("path and data can't be empty at the same time")

'''
检查ip端口是否可用
'''


def do_check(ip, port, backValue):
    try:
        telnetlib.Telnet(ip, port=port, timeout=5)
        backValue.put(ip + ":" + port)
    except Exception as ex:
        print("异常信息：%s" % ex)

'''
执行方法
'''


def main():
    http_proxy_list, https_proxy_list = get_kuaidaili_proxy_list()
    if len(http_proxy_list) == 0 and len(https_proxy_list) == 0:
        print("没有可执行数据")

    if len(http_proxy_list) > 0:
        check_save_proxy("D:\work-self\scrapy-demo\demo\demo\data\http.txt",http_proxy_list)
    if len(https_proxy_list) > 0:
        check_save_proxy("D:\work-self\scrapy-demo\demo\demo\data\https.txt", https_proxy_list)


if __name__ == '__main__':
    main()
