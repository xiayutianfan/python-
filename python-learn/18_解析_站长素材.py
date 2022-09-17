# 请求对象定制
# 获取网页源码
# 下载

# 需求 下载前十页的图片
# https://sc.chinaz.com/tupian/meinvxiezhen.html
# https://sc.chinaz.com/tupian/meinvxiezhen_2.html

import urllib.request
from lxml import etree
import re

def create_request(page):
    if(page == 1):
        url = "https://sc.chinaz.com/tupian/meinvxiezhen.html"
    else:
        # 因为page是int类型, 得要转成string类型才行
        url = "https://sc.chinaz.com/tupian/meinvxiezhen_" + str(page) + ".html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content):
    # 下载图片
    tree = etree.HTML(content)
    # //div[@class='container']//div/img/@src
    # 一般设计图片的网站都涉及到懒加载
    src_list = tree.xpath("//div[@class='container']//div[@class='bot-div']/a/@href")
    # //div[@class='container']//div/img/@alt
    name_list = tree.xpath("//div[@class='container']//div/img/@alt")

    for i in range(len(src_list)):
        name = name_list[i]
        src = src_list[i]
        src = re.findall("[0-9]+", str(src))
        src = "".join(src)
        url = "https://sc.chinaz.com/tupian/" + src + ".htm"
        request = get_src(url)
        content = get_content(request)
        url = down_src(content)
        url = "".join(url)
        # 开始下载图片
        urllib.request.urlretrieve(url=url, filename="./tupian/" + name + ".jpg")
        print(1)

def down_src(content):
    tree = etree.HTML(content)
    # 吐血了, 藏的够深的啊
    src = tree.xpath("//div[@class='right-operation']/p/@data-txt")
    return src



def get_src(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page + 1):
        # 请求对象的参数
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(content)