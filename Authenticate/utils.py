from random import randint, random


def generate_emp_code(N):
    minimum = pow(10, N-1)
    maximum = pow(10, N)-1
    code1 = str(randint(minimum, maximum))
    code = 'VOL' + code1
    print(code)
    # code1 = randint(0,22)
    # code = 'SADEMP' + code1
    return code
