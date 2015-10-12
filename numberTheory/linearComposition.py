def gcd(x, y):
    x = abs(x)
    y = abs(y)
    a = max(x,y)
    b = min(x,y)
    r = a % b
    q = a // b
    if r == 0:
        return {}
    else:
        equation = gcd(b,r)
        equation[r] = [a, -q, b]
        return equation

x = int(raw_input())
y = int(raw_input())
print gcd(x, y)
