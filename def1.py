def power(x,n):#位置参数
	s =1
	while n>0:
		s=s*x
		n=n-1
	return s
print(power(2,3))
def clac(*numbers):#可变参数,传入多个参数
	sum=0
	for n in numbers:
		sum = sum + n*n
	return sum
print(clac(1,2))
#print(clac((1,2,3)))此行代码运行错误，定义可变参数加*号，直接传入tuple或者list
nums =[1,2,3]
print(clac(*nums))#可在list或者tuple前直接加*作为可变参数传入函数