
#IO操作
f = open("words.txt")
#存为字符串
str = f.read()
#分隔并存为list
str_list_all = str.split()
#去重
str_list =list(set(str_list_all))
#保持去重前的顺序
str_list.sort(key=str_list_all.index)

i = 0
for item in str_list:
    conut = str_list_all.count(item)
    print(item,i,conut)
    i =i+1