'''

字符a-z, A-Z可以编码为1-26。"A"->"1", "a"->"1", "B"->"2", "b"->"2", "Z"->"26", "z"->"26"
现在输入一个数字序列，计算有多少种方式可以解码成字符a-zA-Z组成的序列。

例如：

输入：19
输出：6 
(ai, Ai, aI, AI, s, S)

输入：268
输出：12

输入：219
输出：16


'''

def how_many_ways(digitarray):
    # implement here
    