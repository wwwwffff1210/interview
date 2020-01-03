def how_many_ways(digitarray):

    length = len(digitarray)
    #按照该数字的长度生成一个列表
    li = list(range(length+1))
    # 至少一次
    li[0] = 1
    #循环去判断该数字的每一个值
    for i in range(length+1):
        if i == 0:
            continue
        if digitarray[i-1] == '0':
            li[i] = 1
        else:
            li[i] = li[i-1]
        #判断当前字符跟前一个字符是否可以凑成一个字母所对应的值
        if (i>1 and int(digitarray[i-1])<=5 and int(digitarray[i-2])==2) or (i>1 and int(digitarray[i-2])==1):
            li[i] += li[i-2]
    # print(li)
    return li[length]

while True:
    # 用户输入
    digitarray = input('输入: ')

    # 调用函数
    count = how_many_ways(digitarray)

    # 输出
    print('输出:%s'%count)