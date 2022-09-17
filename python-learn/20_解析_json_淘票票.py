import urllib.request

# https://dianying.taobao.com/cityAction.json?city=440100&_ksTS=1661499207020_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true
url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1661499970475_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"

# 前面有冒号 : 都不用能用
headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?city=440100&_ksTS=1661499207020_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 这一行是字符编码问题, 不注释会出现编码格式错误
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.2.3',
    'cookie': 'miid=7827607281826943281; enc=a8kCXz7fk9EwcDikfLrY49JJBFuPw5DYNhmClapG2anqh3KFOuTOqa0zO7AdlerqE2epilcTf2WO78F2Or7RUiLOozh5HHzH5OPECzHyDz%2FiRxDU%2BFiLKWZwleKr%2F4cm; thw=cn; cna=CBfnGhkGdC0CAXW3V+ymkODP; t=5dd4b33eb165a05304e559af77b60619; cookie2=18b37c868d709b55738257249a9e4c37; v=0; _tb_token_=3ee557e875e37; xlly_s=1; tb_city=440100; tb_cityName="uePW3Q=="; tfstk=cuxlBF9vUU77j4pwL3sSxzXlkggAwuUCsQO90YZFIVALlrCcurzwVG3ONfGzR; l=eBx0n_XuLHqTLzLXKOfanurza77OSIRYYuPzaNbMiOCPO4CB5pefW6lT-CY6C3GVhs_wR3klB_nBBeYBqQAonxvTaxom40kmn; isg=BJubr-YUfCru84G9CupOVBI-Kv8FcK9ywwsALI3YchqxbLtOFUE6w6zqBsxikQdq',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.4.32c0112ajbiV65&city=440100',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
    'x-requested-with': 'XMLHttpRequest'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

# 切割
content = content.split("(")[1].split(")")[0]

# 下载
# with open("20_淘票票.json", "w", encoding="utf-8") as fp:
#     fp.write(content)

import json
import jsonpath

obj = json.load(open("20_淘票票.json", "r", encoding="utf-8"))
city_list = jsonpath.jsonpath(obj, "$..regionName")
print(city_list)