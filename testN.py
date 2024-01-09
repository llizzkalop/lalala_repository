def test(*args):
    print('буквы:')
    print('какие-то буквы:',(args))
    print(args)
    for arg in enumerate(args):
        print('итог:',arg)
print(test(15))
#всё ещё не поняла как убрать None :\
def factorial(n):
    if n == 1:
        return 1
    factorial_1 = factorial(n=n - 1)
    return n* factorial_1

print(factorial(15))
