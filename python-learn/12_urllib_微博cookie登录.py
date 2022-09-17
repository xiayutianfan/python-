# 适用场景: 采集数据的时候,需要进入某个页面
# 个人信息页面是utf-8, 但还是报了编码错误, 因为并没有进入个人信息页面, 而是跳转到登录页面了
# 登录页面可能不是utf-8

import urllib.request

# 这个是手机版的微博地址
url = "https://weibo.cn/6579117405/info"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
    # 这个是判断当前路径是不是由上一个路径进来的, 一般情况是做图片防盗链
    "referer": "https://weibo.cn/",
    # cookie携带着登录信息,可以使用cookie免登录
    "cookie": 'XSRF-TOKEN=43hei_WQJSaU_Yv9TSBlCM93; WBPSESS=1QIptkPh0r7VTljIOfRP66kq-ZUM0DeWKSBba4yyhIJcq4_s4BwLEpOmeKLOrN-C0TUXCFCguhaUBQeWVhaCmSqQ1Se1Qu-k9zzJdIoVE9wbbeG_lWhp1kLTtcocTAMJeDL8xpXbaKS77T0WPpvu8rimmL71f83uYYnVqnH37wA=; login_sid_t=7ddbfedb7b87b3c4628ea1b30ca0da8f; cross_origin_proto=SSL; _s_tentry=weibo.com; wb_view_log=1707*10671.5; Apache=6787693978452.982.1661241719421; SINAGLOBAL=6787693978452.982.1661241719421; ULV=1661241719423:1:1:1:6787693978452.982.1661241719421:; ALF=1692777837; SSOLoginState=1661241840; SUB=_2A25OAPmhDeRhGeBL7FsQ8SnIyzmIHXVtdGxprDV8PUNbmtAfLRL3kW9NRsKGW0XHQviVKC1KK4y-1f1S5dw7jfSt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5URPcu0yBJFLycLAR74vUX5JpX5KzhUgL.FoqfS0.peKMXeh-2dJLoIEXLxKBLBonL12zLxK.L1-zLBKnLxK-LBKBLBK.LxKML1heLBKqLxKBLBonLBoqt; wvr=6; wb_view_log_6579117405=1707*10671.5; UOR=,,www.baidu.com; PC_TOKEN=5fd16a2d11; webim_unReadCount={"time":1661242809449,"dm_pub_total":0,"chat_group_client":0,"chat_group_notice":0,"allcountNum":77,"msgbox":0'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# gb2312这个编码格式是请求url的时候, 跳转到登录页面了, 登录页面的编码是gb2312
content = response.read().decode("gb2312")

with open("weibo.html", "w", encoding="utf-8") as fp:
    fp.write(content)