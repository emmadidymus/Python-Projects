def my_function(a,b,/,*,c,d):
    return a+b+c+d

result = my_function(3,5, c=6, d=9)
print(result)