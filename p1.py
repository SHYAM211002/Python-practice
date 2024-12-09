# Lambda function
x = 8
y = 2
z = lambda x,y: x+y
print(z(x,y))


# map function
def even_no(num):
		if num%2 == 1:
			return num+1
		else:
			return num
x = [1,2,3,4,5,6,7,8,9]
#///////////////////////////
#  y = []
# for num in x:
# 	y.append(even_no(num))
# print(y)
# //////////////////////////
y = list(map(even_no, x))
print(y)

#filter function 

#  def over_two(l1)
# l2 = [x for x in l1 if x>2 ]
# return l2
# print over_two([4,3,2,1])
# ////////////////////
n=[4,3,2,1]
print(list(filter(lambda x: x>2, n)))