def Fibonacci(fib):
    if fib > 1:
        return Fibonacci(fib-1) + Fibonacci(fib-2)
    return fib
    
fib=int(input("Inserire numero: ")) 
Fibonacci(fib)

for g in range(1, fib+1):
    print(Fibonacci(g))  