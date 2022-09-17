import urllib.request

#下载网页
url_page = "http://www.baidu.com/"
urllib.request.urlretrieve(url_page, "baidu.html")