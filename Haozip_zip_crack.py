#!/usr/bin/env python
# -*- coding=utf-8 -*- 
#__author__ = 'LF'
# 2016年5月11日 16:10:37
 
import sys, os
import itertools

keylist = """a,b,kk,99"""           # 这里是可能的密码片段
unzipPath = "C:\Users\LF\Desktop"   # 解压到 路径
keylist = keylist.split(",")        # 转为列表存储
keylist_A = []                      # 这里将要存储 排列后的 密码

def factorial(n):   
    ''' # 阶乘  n!=1×2×3×...×n。 亦可以递归方式定义：0!=1，n!=(n-1)!×n。  '''
    if n == 0 : 
        return 1
    else:
        return n * factorial(n-1)

def permutation(n,m):      
    ''' # 排列  A(n,m)= n!/(n-m)! （n≥m)   '''
    return factorial(n)/factorial(n-m)

def combination(n,m):      
    ''' # 组合  C(n,m)= n!/((n-m)!*m!)   (n≥m)    '''
    return permutation(n,m)/factorial(m)

def password_permutation_count(n):      
    ''' # 排列求和  sum_A(n) = A(1,1) + A(2,2) + …… + A(n,n)    '''
    sumA = 0
    for x in range(n):
        sumA = sumA + permutation(n,x+1)
    return sumA

def psw_permutation_combination(keylist=keylist):  
    for m in range(len(keylist)):
        for x in itertools.permutations(keylist, m+1):   # 在 keylist 中，选出 m+1 个元素进行排列     例：permutations('abc', 2)     结果是 'ab','ac','ba','bc','ca','cb'
            #print(list(x))               # list(x) 中存放的是 从keylist 选出 m+1 个元素的列表，例 itertools.permutations(keylist, 2)   结果是 ['a', 'b']  ['a', 'c']  ['b', 'a']  ['b', 'c']  ['c', 'a']  ['c', 'b']
            strc = ""
            for item in list(x):          # 将每个 list(x) 中的元素 组合成一个元素
                strc = strc + "".join(item)    
            #print(strc)     # type(strc)   这里可以看到 组合后的元素结果
            keylist_A.append(strc)        # 组合后的元素 追加到 list 中，构成排列后的密码之一
    print(u" %s 个排列结果 = %s\n"%(len(keylist_A),keylist_A))
    print(u"  共计 %s 个排列组合密码"%len(keylist_A))
    return keylist_A


def try_psw(filename):
    """尝试用密码来解压压缩包"""
    command = ""
    for index,psw in enumerate(keylist_A):
        #command = "C:\Users\LF\Desktop\Haozip\HaoZipC x %s -p%s"%(filename,psw)
        command = "C:\Users\LF\Desktop\Haozip\HaoZipC x -o%s %s -p%s"%(unzipPath,filename,psw)
        ret = os.popen(command).read()
        if ret.decode('gbk').find(u"已完成") != -1:
            print(u"%s 正在尝试 密码 %s --- %s"%(index+1,psw,"Right pass"))
            print("\n")
            print( '        Right psw is : %s'%psw)
            break
        else:
            print(u"%s 正在尝试 密码 %s --- %s"%(index+1,psw,"Wrong pass"))

def goOn_or_stop(filename):
    inp = ""
    while not inp:
        print(u"\n    输入 1 开始破解\n    输入 3 退出程序\n")
        inp = int(input("Your choice : "))
        if inp==1:
            print(u"    开始破解")
            try_psw(filename)
        elif inp ==3:
            print(u"    退出程序")
        else:
            inp = ""

def test():
    '''这里测试了  阶乘，排列，组合，排列求和     '''
    n , m = 4 , 2
    fact = factorial(m)
    print(u" 阶乘  %s! = %s"%(m,fact))

    perm = permutation(n,m)
    print(u" 排列  A(%s,%s) = %s"%(n,m,perm))

    comb = combination(n,m)
    print(u" 组合  C(%s,%s) = %s"%(n,m,comb))
    
    sum_A = password_permutation_count(4)
    print(u" 4 个元素，排列情况 总数 = %s"%sum_A)

    print('\n')
    psw_permutation_combination()


def main(filename):
    psw_permutation_combination()   # 将用户输入的密码片段排列，存入 keylist_A 列表中
    goOn_or_stop(filename)

if __name__ == '__main__':
    #test()

    if len(sys.argv) != 2:
        print('argv error')
        print('usage example : python  try_zip_psw.py  target.zip')
        sys.exit(1)
    main(sys.argv[1])
