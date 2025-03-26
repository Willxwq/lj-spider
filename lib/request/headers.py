#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# USER AGENTS 可以自己添加

import random
from lib.spider.base_spider import SPIDER_NAME

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"
]


def create_headers():
    headers = dict()
    headers["User-Agent"] = random.choice(USER_AGENTS)
    headers["Referer"] = "http://www.{0}.com".format(SPIDER_NAME)
    headers["Cookie"] = "lianjia_uuid=98c2ad1b-b6e7-466a-a712-a46d59c32753; HMACCOUNT=3EF3EBB908947419; _ga=GA1.2.1191921646.1738832017; _jzqc=1; crosSdkDT2019DeviceId=dzmv6z--l8ihjy-hy831x3vtpqgitp-hjhkxpcjt; lfrc_=64a2777d-2d0b-42b9-aca2-a5d31ef37570; _ga_00MKBBEWEN=GS1.2.1739431488.2.0.1739431488.0.0.0; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1741921447; _ga_WLZSQZX7DE=GS1.2.1742526707.1.0.1742526707.0.0.0; _ga_TJZVFLS7KV=GS1.2.1742526707.1.0.1742526707.0.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22194da770429164-0d3b8597fbfda8-1e525636-1296000-194da77042a1d00%22%2C%22%24device_id%22%3A%22194da770429164-0d3b8597fbfda8-1e525636-1296000-194da77042a1d00%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _jzqx=1.1738832020.1742874759.4.jzqsr=hz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=hz%2Efang%2Elianjia%2Ecom|jzqct=/; _ga_34Q2BG9VYB=GS1.2.1742874754.6.1.1742874768.0.0.0; _ga_1W6P4PWXJV=GS1.2.1742874799.2.0.1742874799.0.0.0; _ga_W9S66SNGYB=GS1.2.1742874799.2.0.1742874799.0.0.0; select_city=310000; lianjia_ssid=b63ba59b-0552-4ad1-b42b-8f9a95ec2bbd; _jzqa=1.1047622645621469600.1738832020.1742883678.1742972971.8; _jzqckmp=1; _gid=GA1.2.271277484.1742972983; login_ucid=2000000474710429; lianjia_token=2.0014384e1f42f6a26e0595672ecb159b10; lianjia_token_secure=2.0014384e1f42f6a26e0595672ecb159b10; security_ticket=JGj37ThxoyRx2kE2Qf/Y3Vdh8nKaHszlovrKIZzT0yUZsf8MpGf3/fnvLyst1CdQXQdZKtgyDyccuvUXgIJa5Dc2BTaG/i/GwpJtbbT4cIKdmJ3jlOF4KaUhJ5zUjoNwEvSY2oEJaTEpTlbtPoRPk4qB9XBxP3sP10PitAi9VDA=; ftkrc_=7c95bb66-b47c-4154-b5bf-724b50e6ebbe; _ga_LRLL77SF11=GS1.2.1742972983.6.1.1742979043.0.0.0; _ga_GVYN2J1PCG=GS1.2.1742972983.6.1.1742979043.0.0.0; _jzqb=1.53.10.1742972971.1; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1742979256; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1"
    return headers


if __name__ == '__main__':
    pass
