import math

def get_total_page(m, n):
    return math.ceil(m / n)

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))
