def arb_args(*args):
    for arg in args:
        print(arg)

arb_args("art", "music", "dance", 233, 544, 8964, False, True)


def inner_func(int1, int2):
    def math1 (a,b):
        return a*b
    def math2 (a,b):
        return a+b
    
    value1= math1(int1, int2)
    value2= math2(int1, int2)

    print(value1 + value2)

inner_func(2, 3)


def lunch_lady(name, preference= "Mystery Meat"):
    print(name, preference)


lunch_lady('Bob', 'Ribs')
lunch_lady('Sue')

def sum_n_product(int1, int2):
    sum = int1 + int2
    product = int1 * int2
    return sum, product

print(sum_n_product(2,3))

def alias_arb_args(*args):
    arb_args(*args)

alias_arb_args("art", "music", "dance", 233, 544, 8964, False, True)

def arb_mean(*integers):
    length = len(integers)
    sum = 0
    for integer in integers:
        sum += integer
    mean = sum/length
    print(mean)

arb_mean(1,2,3,4,5,6,7,8,9,10)

def arb_longest_string(*strings):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    print(longest)

arb_longest_string("art", "music", "dance","watermelons", "peanuts")