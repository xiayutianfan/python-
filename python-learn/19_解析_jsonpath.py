import jsonpath
import json

obj = json.load(open("19_解析_jsonpath.json", "r", encoding="utf-8"))
print(obj)
# 查找书店所有的作者
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 查找所有作者
# author_list = jsonpath.jsonpath(obj, '$..author')
# print(author_list)

# store下面的所有元素
# author_list = jsonpath.jsonpath(obj, '$..store.*')
# print(author_list)

# store下的所有price
# price_list = jsonpath.jsonpath(obj, '$..price')
# print(author_list)


#第三个书
# author_list = jsonpath.jsonpath(obj, '$..book[2]')
# print(author_list)

# 最后一本书
# author_list = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# print(author_list)

# 前两本书
# author_list = jsonpath.jsonpath(obj, '$..book[:2]')
# author_list = jsonpath.jsonpath(obj, '$..book[0,1]')
# print(author_list)

# 过滤所有包含isbn的书, 条件过滤得要加 ? 号
# author_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(author_list)

# 查找超过10块钱的书
author_list = jsonpath.jsonpath(obj, '$..book[?(@.price > 10)]')
print(author_list)