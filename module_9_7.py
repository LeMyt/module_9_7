def is_prime(func):
    def analis(a, b, c):
        summa = func(a, b, c)
        if summa <= 1:
            print('Не является ни простым, ни составным')
            return summa
        elif summa == 2:
            print('Простое')
            return summa
        elif summa % 2 == 0:
            print('Составное')
            return summa
        else:
            for i in range(3, int(summa ** 0.5) + 1, 2):
                if summa % i == 0:
                    print('Составное')
                    return summa
        print('Простое')
        return summa
    return analis

@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3

result = sum_three(2, 3, 6)
print(result)