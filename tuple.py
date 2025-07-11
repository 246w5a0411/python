mytuple=(13,12,11)
print(type(mytuple))
mytuple2=()
print(type(mytuple2))
mytuple3=(10,)
print(type(mytuple3))


mytuple1=(12,23,45,34+78j,[12,34,45],"hello",(123,"ece"))
print(mytuple1)
mytuple2=(45,)
print(type(mytuple2))
t=[23,45,56,"jj"]
print(t)
k=tuple(t)
print(k)
t=tuple()
print(t)
#accesing tuples in the tuple
#using the index we can acess the by n-1 rule ....inthis 0:5  given then it takes as 5-1=4 th position..01234 
#elememts in a tuple
#index syntax (start:stop)
mytuple8=(11,22,44,55,77,(78,89),"hello")
print(type(mytuple8))
print(mytuple8[0:5])
print(mytuple8[0:3])
mytuple9=([12,13,14,],(89,90,78))
print(mytuple9[1])
#slicing--it is used to retrive the elememts.. access the tuple using imdex or tuple
#from particular range of syntax
#yntax(tart:stop:skip)s^3..for skip n-1
mytuple10=(11,12,33,45,55,77,89,99,"electronics","hello","communication")
print(mytuple10[1:7:2])
#indexing are two types.. postive indexing negative..it starts with 0  from left hand side
#negative indexing/backward indexing.. it start with  from right hand direction
mytuple12=("hello",123,456,45,34.45,56+78j,"lists","agri","ece",345.9,"dept",12,23,34)
mytuple=(12,[12,13],(10,20))
print(mytuple)
print(mytuple[1][1])
print(mytuple[2][1])