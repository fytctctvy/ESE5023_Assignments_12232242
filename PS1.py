#!/usr/bin/env python
# coding: utf-8

# In[67]:


#  1. Flowchart
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        elif a>c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif b<=c:
        print(c,b,a)
import random
a = random.randint(0,50)
b = random.randint(0,50)
c = random.randint(0,50)
print("a:",a,"\nb:",b," \nc:",c)
Print_values(a,b,c)


# In[71]:


#  2. Matrix multiplication
#  2.1 
import numpy as np
M1 = np.random.randint(0,50,(5,10))
M2 = np.random.randint(0,50,(10,5))
print("M1: \n",M1)
print("M2: \n",M2)


# In[72]:


#  2.2 
def Matrix_multip(M1,M2):
    import numpy as np
    row1 = 5
    column1 = 5
    #  K为M1的行数及M2的列数
    K = 10
    M3 = np.zeros((row1,column1))
#  使用三重for循环时，我参考了网址：https://blog.csdn.net/m0_52025744/article/details/121947127
    for i in range(row1):
        for j in range(column1):
            for k in range(K):
                M3[i,j] = M3[i,j] + M1[i,k] * M2[k,j]
    print (M3)
Matrix_multip(M1,M2)


# In[73]:


#  3. Pascal triangle
N = [1]
Rows = 100 
#  当行数为200时，将上行Rows的值改为200

for i in range(Rows):
    N.append(0)
    N = [N[K]+N[K-1]for K in range(i+1)]
print(N)
#  以下结果目前显示的是第100行的数字集


# In[74]:


#  4. Add or double
def Least_moves(a):
    if a%2 ==0:
        return Least_moves(a/2)+1
    elif a==1:
        return 0
    else:
        return Least_moves(a-1)+1
Least_moves(5)
print(Least_moves(5))


# In[75]:


#  5. Dynamic programming
# 5.1
import numpy as np
N1 = np.random.randint(0,100)
print(N1)
def Find_expression(num):
    dig = "123456789"
    opration = ['+', '-', '']
    def All_expression(dig):
        if len(dig) == 1:
            return [dig] 
        else:
            return [dig[0] + j + i for i in All_expression(dig[1:]) for j in opration]
    return [i for i in All_expression(dig) if eval(i) == N1]
print(Find_expression(N1))

#  以下结果说明当输入值等于67时，有以下15个式子可以通过加减运算得到67


# In[76]:


#  5.2
Total_solutions=[]
for N2 in range(1,101):
    def Find_expression(num):
        dig = "123456789"
        opration = ['+', '-', '']
        def All_expression(dig):
            if len(dig) == 1:
                return [dig] 
            else:
                return [dig[0] + j + i for i in All_expression(dig[1:]) for j in opration]
        return [i for i in All_expression(dig) if eval(i) == N2]
    Total_solutions.append(len(Find_expression(N2)))
print(Total_solutions)
#  以上代码基本与5.1相同，仅将输入随机数改为：依次输入1到100。并添加了一步：计算list中的元素个数，即输入的数字对应的Total_solutions的个数

# 使用matplotlib模块画坐标图时，我参考了网址：https://blog.csdn.net/HHG20171226/article/details/101294381
# 横坐标为输入的数字，纵坐标为数字对应的解决方式的总数
import matplotlib.pyplot as plt
import numpy as np

x_axis_data = list(range(1,101))
y_axis_data = Total_solutions

plt.plot(x_axis_data, y_axis_data, '-', alpha=1, linewidth=1)
plt.xlabel('digits') 
plt.ylabel('Total_solutions')
plt.ylim(-1,31)
plt.xlim(0,101)
plt.show()
#  以下集合是1-100按顺序所对应的Total_solutions，为了更好看清图片，横纵坐标的范围，左右均扩大了1个单位,
#  可以看出Total_solutions（max）=26 对应的数字是1和45； Total_solutions（min）=6 对应的数字是88

