#funciones utilitarias 
print(list(range(0,100,10)))

print(list(range(0,100,10)))


#Enumaerate
for i, letter in enumerate('abcde'):
  print("indice {} la letra {}".format(i, letter))


#Zip
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

print(list(zip(mylist1,mylist2)))


#min = max
mylist = [10,20,30,40,100]

print(min(mylist))
print(max(mylist))