#!/usr/bin/env python3

even_fibo_set = {2}

def fibonnaci(x, y):
    if x % 2 == 0:
         even_fibo_set.add(x)
    if y % 2 == 0:
        even_fibo_set.add(y)
    next_in_sequence = x + y
    x = y
    if next_in_sequence <= 4000000:
        fibonnaci(x, next_in_sequence)

fibonnaci(1,2)
print(sum(even_fibo_set))