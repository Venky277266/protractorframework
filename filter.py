#Filter FPT

'''l = [2,4,5,6,7,8,9]
def odd(a):
	return a%2 != 0
print(filter(odd,l))
#print(list(filter(odd,l)))'''

#Map FPT

'''salary = [10000 , 20000, 30000]
def hike(salary):
	return (salary+(salary*10/100))
print(map(hike,salary))
#print(list(map(hike,salary)))'''

#Reduce FPT

from functools import reduce
"""
salary = [10000 , 20000 , 30000]
def get_sum_salary(s1,s2):
	print(s1,s2,s1+s2)
	return s1+s2
print(reduce(get_sum_salary,salary))
"""
"""salary = [10000 , 20000 , 30000 , 40000 , 50000]
def sum_of_salary(s1,s2):
	print(s1,s2,s1+s2)
	return s1+s2
print(reduce(sum_of_salary , salary))"""

#my_list = [10,40,20,67,80,96]
#my_list1 = list(filter(lambda n : n%5 == 0 , [30,50,78,93,67,80,30,65]))
#print(my_list1)
print(list(map(lambda n : n+(n*10)/100 , [10000,20000,30000])))
#print(increment_salary)


