#参数的定义，参数的定义顺序是：必选参数，默认参数，可变参数/命名关键字参数和关键字参数

#位置参数
def power(x,n):
	s =1
	while n>0:
		s=s*x
		n=n-1
	return s
print(power(2,3))


#可变参数,传入多个参数
def clac(*numbers):
	sum=0
	for n in numbers:
		sum = sum + n*n
	return sum
print(clac(1,2))
#print(clac((1,2,3)))此行代码运行错误，定义可变参数加*号，直接传入tuple或者list
nums =[1,2,3]
print(clac(*nums))#可在list或者tuple前直接加*作为可变参数传入函数


#关键字参数
exat={'city':'beijing','job':'teacher'}
def person(name,age,**exat): #此处**定义了关键字参数,传入函数自动组装为dict，可大大扩展函数的功能
	print('name:',name,'age:',age,'other:',exat)
person('张三',25,**exat)


#命名关键字参数
def per(name,age,*,city,job):#可有缺省值，在定义函数时定义
	print(name,age,city,job)
per('李四',22,city='beijing',job='teacher')