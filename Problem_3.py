#!/usr/bin/env python3

prime_factors = {1}

def find_factors(x):
    factors = {1,x}
    for i in range(1,x+1):
        if x%i == 0:
            factors.add(i)
    print(factors)
    return factors


def find_prime_factors(factor_set):
    global prime_factors
    for f in factor_set:
        f_factors = find_factors(f)
        if len(f_factors) == 2:
            prime_factors.update(f_factors)


factors = find_factors(53)
find_prime_factors(factors)
prime_list = list(prime_factors)
print(prime_list[len(prime_list)-1])