# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword
# post 请求
# cname:
# pid:
# keyword: 上海
# pageIndex: 1
# pageSize: 10

import urllib.request
import urllib.parse

def create_request(page):
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    data = {
        "cname": "",
        "pid": "",
        "keyword": "上海",
        "pageIndex": page,
        "pageSize": "10"
    }

    data = urllib.parse.urlencode(data).encode("utf-8")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
    }
    request = urllib.request.Request(url=base_url, headers=headers, data=data)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

def down_load(page, content):
    with open("KFC_" + str(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页数"))
    end_page = int(input("请输入结束页数"))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # # 获取网页源码
        content = get_content(request)
        # # 下载
        down_load(page, content)