import math
#函数学习
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(2))

def move(x,y,step,angle=0):
	nx = x+step * math.cos(angle)
	ny = y-step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)

def quadratic(a,b,c):
	if (b*b)-(4*a*c)>0:
		print('one:',(-b-math.sqrt((b*b)-(4*a*c)))/(2*a))
		print('two:',(-b+math.sqrt((b*b)-(4*a*c)))/(2*a))
	else:
		print('no result')
a=1
b=3
c=-4
print(quadratic(a,b,c))