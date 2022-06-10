import itertools

#二维平面的分割，问题的解决思路为：根据小平面所有排列组合的结果根据长、宽、面积的约束筛选出最优结果

#限制平面的大小如下
X_Area=2256
X_length=48.0
X_width=47.0
#小平面的规格如下
x={14.00001:14,
   14.0000001:21,
   14.001:28.00001,
   7.00001:28,
   7.000001:14.001,
   21.00001:28.001,
   21.000001:35,
   15.00001:30,
   15.000001:30.00001,
   
    14:14.00001,
   21:14.0000001,
   28.00001:14.001,
   28:7.00001,
   14.001:7.000001,
   28.001:21.00001,
   35:21.000001,
   30:15.00001,
   30.00001:15.000001}
'''小盒子的规格有14*14，7*14，15*30，21*35，21*28，7*28，14*28，21*14，共八种'''
#根据小平面的长宽组成排列组合的元素
x_length=list(x.keys())
x_width=list(x.values())
#横放和竖放
L=x_length+x_width
W=x_width+x_length

for i in range(1,len(L)+1):
    iter=itertools.combinations(L,i)#任意组合
    #iter=itertools.permutations(L,i)#任意排列
    #length_array.append(list(iter))
    length_array=[]
    width_array=[]
    D_value_array=[]
    for tuple_i in iter:
        new_dic={}
        temp_array=[]
        length_sum=0
        width_sum=0
        Area=0
        for j in tuple_i:
            length_sum=length_sum+j
            width_sum=width_sum+x[j]
            Area=Area+i*x[j]
            temp_array.append(x[j])
        D_valueL=X_length-length_sum
        D_valueW=X_width-width_sum
        D_value_Area=X_Area-Area#增加面积判断
        if D_valueL>=0.0 and D_valueL<=5.0 and D_valueW>=0.0 and D_valueW<=5.0 and D_value_Area>0 and D_value_Area<100:#收敛
            for k in tuple_i:    #满足收敛条件的长和宽(小箱子)
                new_dic[k]=x[k]
            length_array.append(tuple_i)  #满足收敛条件的长度集合
            width_array.append(temp_array)    #满足收敛条件的宽度集合
            if len(new_dic)>0:
                with open(r'C:\adsfadgadfasdfasdga.txt','a') as save_result:  #设置保存结果的文件路径
                    print('----------------------------------------分割线----------------------------------------------------------------------------')
                    print("[+]：符合条件的小箱子是")
                #print(new_dic)
                #print('总长为{}，总宽为{}'.format(length_sum,width_sum))
                #print('[-]：它们的误差是：长的为{}，宽的为{}\n'.format(D_valueL,D_valueW))
                    save_result.write('----------------------------------------分割线----------------------------------------------------------------------------\n')
                    save_result.write("[+]：符合条件的小箱子是\n")
                    for item in list(new_dic):
                        save_result.write(str(item)+'\n')
                    save_result.write('总长为{}，总宽为{}\n'.format(length_sum,width_sum))
                    save_result.write('[-]：它们的误差是：长的为{}，宽的为{}\n'.format(D_valueL,D_valueW))
#以下为冗余代码
            '''
    if len(length_array)>0 and len(width_array)>0:
        print('----------------------------------------分割线----------------------------------------------------------------------------')
        print("[+]：满足收敛条件的长为")
        print(length_array)
        print()
        print("[+]：满足收敛条件的宽为")
        print(width_array)
        print()
'''
