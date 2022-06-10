import itertools
#从面积角度判断符合条件的结果
X=2256 #大区域的面积
x=(196,294,392,98,588,735,450)#小区域面积的集合
D_value_array=[]
for i in range(1,len(x)+1):
    iter=itertools.combinations(x,i)
    for tuple_i in iter:
        sumer=0
        #D-value=0
        for j in tuple_i:
            sumer=sumer+j
        D_value=X-sumer
        D_value_array.append(D_value)
        if D_value>0 and D_value<100:
            print('[+]：符合收敛条件的箱子组合是：')
            print('[-]：该组合的误差值为；{}'.format(D_value))
            print(tuple_i)
