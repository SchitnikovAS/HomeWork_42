def is_prime(func):
    def wrapper(*args, **kwargs):
        result_f = func(*args, **kwargs)
        for i in range(2, result_f):
            if result_f % i == 0:
                print('Составное')
                break
            if i == result_f - 1:
                print("Простое")
        return result_f

    return wrapper


@is_prime
def sum_three(a, b, c):
    summ = a + b + c
    return summ


result = sum_three(2, 3, 6)
print(result)
