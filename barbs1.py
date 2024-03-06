my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def la(x):
    return x % 2
def ma(x):
    return x * x
result = map(ma,filter(la, my_numbers))
print(list(result))