import os
import random
import urllib
import urllib.request
import urllib.parse
import re


class Spider:
    # 初始化
    def __init__(self):
        self.base_url = "http://www.benziku.cc/shaonv/"  # 基础url
        self.save_path = "d:/"
        self.num = 0           # 总次数
        self.success_num = 0   # 成功次数

    # 根据url读取页面内容,如果失败则返回False
    def get_page(self, url):
        self.num += 1
        try:
            request = urllib.request.urlopen(url)
        except:
            return False
        print("正在进行第" + str(self.num) + "爬取,url[" + url + "]...")
        if request.getcode() != 200:
            print("爬取失败,错误代码:[" + request.getcode() + "]")
            return False
        else:
            self.success_num += 1
            print("爬取成功,正在分析网页内容...")
            return request.read().decode("utf-8")

    # 分析页面,获取图片链接集合
    def analysis(self, data):
        pattern = re.compile(r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>""", re.S)
        images = re.findall(pattern, data)
        print("正在爬取网页图片,[" + str(images) + "]")
        return images

    # 获取图片链接集合
    def get_images(self, index):
        imgs = []
        url = self.base_url + str(index) + ".html"
        result = self.get_page(url)
        if result:
            imgs.append(self.analysis(result))
            for i in range(2, 100):
                url = self.base_url + str(index) + "_" + str(i) + ".html"
                result = self.get_page(url)
                if result:
                    imgs.append(self.analysis(result))
                else:
                    break
        return imgs

    # 创建目录
    def mkdir(self, index):
        path = self.save_path + str(index)
        if not os.path.exists(path):
            os.mkdir(path)
        print("正在创建文件夹,名称为:[" + str(index) + "], 路径为[" + path + "]")
        return path

    # 保存文件
    def save_file(self, path, file_name, url):
        if "http" not in url:
            return
        u = urllib.request.urlopen(url)
        data = u.read()
        if data is None:
            return
        if not path.endswith("/"):
            path += "/"
        file = open(path + str(file_name) + ".jpg", "wb")
        print("正在保存图片,名称为:[" + str(file_name) + ".jpg" + "]")
        file.write(data)
        file.flush()
        file.close()

    def execute(self, index):
        path = self.mkdir(index)
        images = self.get_images(index)
        for x in images:
            for y in x:
                self.save_file(path, random.randint(1, 999), y)
        print("爬取结束,总计:[" + str(self.num) + "]次, 成功:[" + str(self.success_num) + "]次")

spider = Spider()
spider.execute(6647)
# spider.save_file("d:/6647", "xxx.jpg", "http://bz.juwen.cc/uploads/allimg/160421/1-160421113334412.JPG")