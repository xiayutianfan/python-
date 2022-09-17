# pip install scrapy -i https://pypi.douban.com/simple

#  报错的话
'''
    安装过程中出错：
    如果安装有错误！！！！
    pip install Scrapy
    building 'twisted.test.raiser' extension
        error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++
        Build Tools": http://landinghub.visualstudio.com/visual‐cpp‐build‐tools
    解决方案：
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    下载twisted对应版本的whl文件（如我的Twisted‐17.5.0‐cp36‐cp36m‐win_amd64.whl），
    cp后面是python版本，
    amd64代表64位，运行命令：
    pip install C:\Users\...\Twisted‐17.5.0‐cp36‐cp36m‐win_amd64.whl
    pip install Scrapy
    如果再报错
    python ‐m pip install ‐‐upgrade pip
    如果再报错 win32
    解决方法：
    pip install pypiwin32
    再报错：使用anaconda
    使用步骤：
    打开anaconda
    点击environments
    点击not installed
    输入scrapy
    apply
    在pycharm中选择anaconda的环境
'''


