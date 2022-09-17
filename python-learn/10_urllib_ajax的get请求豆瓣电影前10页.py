import urllib.request
import urllib.parse

def create_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action="
    data = {
        "start": (page - 1) * 20,
        "limit": 20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
        "Cookie": "route-cell=ksa; ASP.NET_SessionId=bl5aagzftwtyt3wkivjior2e; SERVERID=02f4c994014ba2083ffa81762e56b1a0|1661240563|1661239648"
    }

    request = urllib.request.Request(url = url, headers = headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("douban" + str(page) +  ".json", "w", encoding = "utf-8") as fp:
        fp.write(content)


# 程序的入口
if __name__ == "__main__":
    start_page = int(input("请输入起始页数"))
    end_page = int(input("请输入结束页数"))

    for page in range(start_page, end_page + 1):
#         每页都有自己请求对象的定制
        request = create_request(page)
#       获取响应的数据
        content = get_content(request)
#       下载数据
        down_load(page, content)