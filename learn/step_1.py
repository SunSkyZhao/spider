# encoding:UTF-8
import urllib.request

# 用Python抓取指定页面
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

