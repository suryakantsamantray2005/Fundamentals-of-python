import functools
a=functools.reduce(lambda x,y: x if x>y else y,[23,11,45,10,1])
print(a)