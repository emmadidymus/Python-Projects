def my_function(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(my_function(1,2,3))
print(my_function(45,67,89))
print(my_function(90,23,18))