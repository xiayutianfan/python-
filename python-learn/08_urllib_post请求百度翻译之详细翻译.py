import urllib.request
import urllib.parse
import json

# post请求

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token': '1661151781547_1661235483004_0f9CZMIZ5F98s+p/e4nt/8nbrZ+AlxwEaULsxFVtWLyXY5q1G9TLC9A94gcj+3pNbT9maF1j+iqywD1ReX5S2xJ4XVhHgh2AoNNoG3kKPIvkKt1xg5LC/q465CS7LldtgttX5nofbb70w8UmDPh3X9MMpG6cS2n7mXSuYpMhVnY1cpxCBns5DadjYw5pXHH44JRXl+nS9f85tGlk4Zm+8o7WcbV+vY29wnySTJV8PgPjvlN52oF1+iZit9x3DPx9j9athQI4XIGqxs8+TTVxpEFBttYtZbnHXLpU49Rmx+vzpJe4lHHjyNlqn3E4JUCkOmXE5xiOJXNvww4IfdMAuhKrm4xoAgHAM5YFOhH03jg=',
    'Connection': 'keep-alive',
    'Content-Length': '117',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=EB22B91AC066C48DCBFFB91E5688CE15; PSTM=1650465892; newlogin=1; BDUSS=JDZXNpeVdlM1poRThrS3dCdi1ueWcwd0NtNjZoeVYwWkpkTlEyZE53fjR0fmhpRVFBQUFBJCQAAAAAAAAAAAEAAAATCWcY2K3O9MjV2K3s4cnx1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgq0WL4KtFiQX; BDUSS_BFESS=JDZXNpeVdlM1poRThrS3dCdi1ueWcwd0NtNjZoeVYwWkpkTlEyZE53fjR0fmhpRVFBQUFBJCQAAAAAAAAAAAEAAAATCWcY2K3O9MjV2K3s4cnx1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgq0WL4KtFiQX; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=36548_37112_36884_36917_37003_37136_26350_36864_22158; BA_HECTOR=2la4812l80a0ah0g2l0hfe6a1hg8r5q17; BAIDUID_BFESS=C1B7E585E91BE6E4CA4EE7229DAE234C:FG=1; ZFY=g4O:BLO08H:BEBIRRyKK3:AQWRyJC0EGYe:B2qeKiXvUhtE:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1661234613; ab_sr=1.0.1_ZDRjOWY3OTE4NDkxMTRlZjAxYjc5ZTRhNzJlYzAzY2IxZTM0YzVlNmFkMDk3ZmE1Y2VhMDFiODJiNjU4YjY1NWEyZTNmYjBiNmZlZDFhYmJhMzg4YWE1NzFmNTRhNzlkMWI3NWViZTUxMmMyZWM4YjUxNzE4MWM4NTExZTRmMDhiNzIyM2I1YjAwMGFkMTQyZjY5MDRhYjQyMzM1ZTVkZGNkZGQ5YmQ0YWI0NjM5Mzg3N2E2ZjgzZjY4ZjQzMmU3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1661235483; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=C1B7E585E91BE6E4CA4EE7229DAE234C:FG=1',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    "from":"en",
    "to":"zh",
    "query":"china",
    "simple_means_flag":"3",
    "sign":"596529.915712",
    "token":"616271d020181be54cde10542fe86edc",
    "domain":"common"
}

# post请求的参数, 必须要进行编码
data = urllib.parse.urlencode(data).encode("utf-8")

# post请求是不会拼接在url后面的, 而是需要放在请求对象定制的参数中
request = urllib.request.Request(url = url, data = data, headers = headers)

# 发送请求

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

obj = json.loads(content)

print(obj)

