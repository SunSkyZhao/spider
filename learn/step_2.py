# python简单处理url

import urllib
import urllib.request

# 生成字典
data = {}
data['word'] = 'Jecvay Notes'

# 转换成 "word = Jecvay Notes" 的字符串
url_value = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_value

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)