import math
def primesNumber(n):
    array = range(2, n+1)
    number_of_primes = int(n / math.log(n))
    for idx in range(number_of_primes):
        prime = array[idx]
        if prime > math.sqrt(n):
            break
        array = [prime]+[x for x in array if not x%prime == 0]
        array = sorted(array)
    return " ".join(str(x) for x in array)


print primesNumber(int(raw_input()))
