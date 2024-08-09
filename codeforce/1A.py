import math

def solve1A(n, m, a):
    return math.ceil(n / a) * math.ceil(m / a) 

if __name__ == '__main__':
    inp = input()
    list_number = inp.split(' ')
    list_number = list(map(int, list_number))
    n, m, a = list_number
    print(solve1A(n, m, a))