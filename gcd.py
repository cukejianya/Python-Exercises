def gcd(x, y):
    x = abs(x)
    y = abs(y)
    a = max(x,y)
    b = min(x,y)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b,r)

x = int(raw_input())
y = int(raw_input())
print gcd(x, y)
