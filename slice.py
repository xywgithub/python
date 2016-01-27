l=['mick','john','tolnks']
print(l[0:2])
print(l[-1])
li=list(range(100))#0-99的数列
print(li[:10])   #从0开始可缺省
print(li[-10:-2]) #还可以倒数着来
print(li[10:20:2]) #第三个元素2控制增量 即此输出为索引从10,12,14...20的数
tuple=(1,2,3,4,5)
print(tuple[1:2])#tuple切片取出仍然是tuple形式
a='xhabbakf'
print(a[1:3])#字符串也可以使用切片取，结果仍然是字符串


name = ['Adam','Alex','Amy','Bob','Boom','Candy','Chris','David','Jason','Jasonstatham','Bill'];#输入补全
i_name = input("please input name : ").title();
wname = [];
for n in name:
    if n[0:len(i_name)] == i_name:
        wname.append(n);

if len(wname) != 0:
    print('Do you want to find %s?'%(wname));
else:
    print('%s not find'%(i_name));


for x,y in enumerate(['A','B','C']):   #enumerate函数可以把list变成索引-值的形式
	print(x,y)