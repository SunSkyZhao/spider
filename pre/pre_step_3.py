# python队列
from collections import deque
queue = deque(["one","two","three"])
queue.append("four")
queue.append("five")
queue.popleft()  #弹出队首元素
# 输出"one"
queue.popleft()
# 输出"two"
queue.pop()
# 输出deque(["three","four","five"])

# python的数据集合和set()的用法
basket = {"one","one","two","three","three","four"}
print(basket)  #展示去重复功能

# 查找功能
if "one" in basket:
    print("one in there")
else:
    print("oue out there")

# 两个集合的计算
a = set('asdfghjkl')
b = set('hjkbnmuio')
print(a-b) #只在集合a中的元素
print(a|b) #集合a和集合b中的所有元素
print(a&b) #集合a和集合b中的共有元素
print(a^b) #不同时包含于集合a和集合b中的元素

