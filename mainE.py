def primo(n):
    for x in range(2, n):
        check = int(n/x)
        if check * x == n: return False
    return True
t = input("dammi numero ")
t = int(t)
m = primo(t)
print(m)