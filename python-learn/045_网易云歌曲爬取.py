# 大前提, VIP歌曲不行, 会出现404错误

# pip install requests
import requests
# 导入正则表达式
import re
# 文件操作模块
import os


fileName = 'music\\'
# 如果没有这个文件夹, 则创建一个新的文件夹
if not os.path.exists(fileName):
    os.mkdir(fileName)

# 如果要爬取其他的,改这里就可以
url = "https://music.163.com/discover/toplist?id=3778678"
# 伪装成浏览器
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}
#   挂了VPN后这个要加上, 不然会报错(我也不晓得是什么原因)
requests = requests.Session()
requests.trust_env = False

response = requests.get(url=url, headers=headers)
# print(response.text)
# 到response.text里匹配
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a></li>', response.text)
# 经过正则表达式提取出来的内容, 返回的是列表, 里面每个元素都是元组
for num_id, title in html_data:
    music_url = f"https://music.163.com/song/media/outer/url?id={str(num_id)}.mp3"
    # 对音乐播放器发送请求, 获取二进制数据内容(.content)
    music_content = requests.get(url=music_url, headers=headers).content
    # wb 二进制的方式进行保存
    with open(fileName + title + '.mp3', mode='wb') as f:
        f.write(music_content)

print("下载完成~")