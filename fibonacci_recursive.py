n = 50

fibonacci_map = {
    0: 1,
    1: 1
}

# recursion
def fib(x):
    if fibonacci_map.get(x) != None:
        return fibonacci_map.get(x)
    else:
        rhs = fib(x-2)
        fibonacci_map[x-2] = rhs 
        lhs = fib(x-1)
        fibonacci_map[x-1] = lhs
        return lhs + rhs

output = fib(n)
print('output = ' + str(output))
