n = 50

fibonacci_map = {
    0: 1,
    1: 1
}

def fib(x):
    if fibonacci_map.get(x) != None:
        return fibonacci_map.get(x)
    return fib(x-1) + fib(x - 2)

# loop
m = 2
output = 0
while m <= n:
    output = fib(m)
    fibonacci_map[m] = output
    m += 1

print(str(output) + '\n\n\n')

z = 0
while z <= 50:
    print(str(z) + ': ' + str(fibonacci_map[z]))
    z += 1







