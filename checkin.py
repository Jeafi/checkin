import urllib.request
import urllib
import gzip
import http.cookiejar


# 定义一个方法用于生成请求头信息，处理cookie
from pip.cmdoptions import pre


def getOpener(head):
    # deal with the Cookies
    # <pre ame = "code" class ="python">
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


# 定义一个方法来解压返回信息
def ungzip(data):
    try:  # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


# 封装头信息，伪装成浏览器
header = {
    'Proxy-Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': '',
}

url = ''
opener = getOpener(header)

id = ''  # 你的用户名
password = ''  # 你的密码
postDict = {
    'email': id,
    'passwd': password,
}

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data)

url = ''  # 签到的地址
opener.addheaders[2] = ''
op = opener.open(url)

data = op.read()
data = ungzip(data)

print(data)
