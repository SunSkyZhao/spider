# 保存爬取的文本

import re

class Save:
    def save_file(data):
        save_path = 'D;\test.txt'
        f_obj = open(save_path, 'wb')
        f_obj.write(data)
        f_obj.close()