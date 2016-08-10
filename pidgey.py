import os

# todo написать обработку на случай ввода неверных символов или цифр,
#                         не используемых в данной системе счисления

# Функция выбора системы счисления
def get_num_system(msg):
    while True:
        print()
        num_system = print(msg)
        num_system = input('>>>')
        num_system = num_system.upper()
        if num_system == 'BIN':
            return 2
        elif num_system == 'OCT':
            return 8
        elif num_system == 'DEC':
            return 10
        elif num_system == 'HEX':
            return 16


# Функция перевода из двоичной системы
def convert_from_bin(_value, _num_system):
    if _num_system == 2:
        return _value
    elif _num_system == 8:
        return oct(int(_value, 2))
    elif _num_system == 10:
        return int(_value, 2)
    elif _num_system == 16:
        return hex(int(_value, 2))


# Функция перевода из восьмеричной системы
def convert_from_oct(_value, _num_system):
    if _num_system == 2:
        return bin(int(_value, 8))
    elif _num_system == 8:
        return _value
    elif _num_system == 10:
        return int(_value, 8)
    elif _num_system == 16:
        return hex(int(_value, 8))


# Функция перевода из десятичной системы
def convert_from_dec(_value, _num_system):
    if _num_system == 2:
        return bin(int(_value))
    elif _num_system == 8:
        return oct(int(_value))
    elif _num_system == 10:
        return int(_value)
    elif _num_system == 16:
        return hex(int(_value))


# Функция перевода из шестнадцатеричной системы
def convert_from_hex(_value, _num_system):
    if _num_system == 2:
        return bin(int(_value, 16))
    elif _num_system == 8:
        return oct(int(_value, 16))
    elif _num_system == 10:
        return int(_value, 16)
    elif _num_system == 16:
        return _value


def main():
    msg = 'Выберите начальную систему счисления: BIN, OCT, DEC, HEX'
    fnum_system = get_num_system(msg)  # Получаем исходную систему исчисления
    print('Перевод из %sой системы\n' % fnum_system)
    print('Введите значение:')
    value = input('>>>')  # Получаем исходное число
    msg = 'Выберите систему счисления для результата: BIN, OCT, DEC, HEX'
    # Получаем систему счисления, в которую необходимо перевести
    snum_system = get_num_system(msg)
    rows, columns = os.popen('stty size', 'r').read().split()
    msg = str(int(columns) * '=')
    print(msg)
    print('Результат вычислений:')
    if fnum_system == 2:
        print (convert_from_bin(value, snum_system))
    elif fnum_system == 8:
        print (convert_from_oct(value, snum_system))
    elif fnum_system == 10:
        print (convert_from_dec(value, snum_system))
    elif fnum_system == 16:
        print (convert_from_hex(value, snum_system))


main()
