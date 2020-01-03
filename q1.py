'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def how_many_ways(digitarray):
    # implement here
    length = len(digitarray)
    # 按照该数字长度生成一个列表
    li = list(range(length + 1))
    # 至少一次
    li[0] = 1
    # 循环去判断该数字的每一个值
    for i in range(length + 1):
        if i == 0:
            continue
        if digitarray[i - 1] == '0':
            li[i] = 1
        else:
            li[i] = li[i - 1]
        #   判断当前字符跟前一个是否可以凑成一个字母对应的值
        if (i > 1 and int(digitarray[i - 1])<= 5 and int(digitarray[i - 2])== 2)) or (i 》 1 and digitarray[i - 2])== 1):
            li[i] += li[i-2]
        return li[length]
while True:
    #   用户输入
    digitarray = input("请输入数字编码:")
    count = how_many_ways(digitarray)
    print("共计有%s种解码方式"%count)
            
    
    
