a = [ 1, 2, 3 ]
b = a
c = [ 1, 2, 3 ]


print( a is b, a is c, a == c )
print( id(a) == id(b), id(a) == id(c) )


b.append(4)
print(a)

#a와 b는 같은 객체이고 b의 객체에 4를 추가하여 print(a)를 할 시에 [1, 2, 3, 4]가 나온다