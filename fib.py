def fib(n):
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[-2]+fib[-1])
    return fib

def fibsq(n)
    f = fib(n)
    return [n**2 for n in f]

def fib_times_2(n):
    f = fib(n)
    return [n*2 for n in f]
