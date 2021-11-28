number = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90
}

value = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    50: "пятьдесят",
    60: "шестьдесят",
    70: "семьдесят",
    80: "восемьдесят",
    90: "девяносто"
}

operators = {
    'плюс': '+',
    'минус': '-',
    'умножить_на': '*',
    'скобка_открывается': '(',
    'скобка_закрывается': ')'

}

priority = {'+': 0, '-': 0, '*': 1, '(': 10, ')': 10}


def operation_calc(nums, operator):
    right = nums.pop()
    left = nums.pop()
    if operator == '+':
        return left + right
    if operator == '-':
        return left - right
    if operator == '*':
        return left * right


def num_to_str(exp):
    if not -100 < exp < 100:
        return f'Результат вне границ диапазона [-99; 99]. Числовой результат: {exp}.'
    if abs(exp) in value:
        return f"{'минус ' if exp < 0 else ''}{value[abs(exp)]}"
    result = abs(exp) // 10 * 10, abs(exp) % 10
    return f"{'минус ' if exp < 0 else ''}{value[result[0]]} {value[result[1]]}"


def calc_internal(exp):
    exp = exp.replace("умножить на", "умножить_на").replace("скобка открывается", "скобка_открывается").replace(
        "скобка закрывается", "скобка_закрывается").split()
    symbols = []  # складываем сюда числа и операторы (не словестные)
    num = 0  # копим число, если оно составное
    previous_is_num = False  # флаг, если предыдущее -- число
    inverse = False  # надо ли инвертировать число, для отрицательных чисел
    # заменим все слова на символы
    for token in exp:
        if token in number:
            num += number[token]
        elif token in operators:
            if previous_is_num:
                symbols.append(-num if inverse else num)
                num = 0
                inverse = False
            if not previous_is_num and operators[token] == '-':
                inverse = True
            else:
                symbols.append(operators[token])
        else:
            return 'Ошибка! Неизвестное слово:' + token
        previous_is_num = token in number

    if previous_is_num:
        symbols.append(-num if inverse else num)

    # вычисление через обратную польскую запись
    operators_stack = []
    num_stack = []
    for s in symbols:
        if s not in priority:  # не является оператором, значит число
            num_stack.append(s)
            continue
        while len(operators_stack) > 0 and (priority[operators_stack[-1]] >= priority[s]
                                            and operators_stack[-1] != '(' or s == ')'):
            head = operators_stack.pop()
            if head == '(':
                break
            num_stack.append(operation_calc(num_stack, head))

        if s != ')':
            operators_stack.append(s)

    while len(operators_stack) > 0:
        head = operators_stack.pop()
        if head == '(':
            continue
        # back.append(head)
        num_stack.append(operation_calc(num_stack, head))

    return num_stack[-1]


def calc(expression):
    return num_to_str(calc_internal(expression))


print('Доступны базовые операции (плюс, минус, умножить на).\n'
      'Диапазон выводимых значений: [-99, 99].\n'
      'Внимание! Программа не поддерживает обработку некорректных значений (пункт 10 не реализован)!\n'
      'Выполнены пункты: 3 (на три балла), 4 (на три балла), 5 (на один балл)).\n')
try:
    print(calc(
        'пять минус девять умножить на три умножить на три умножить на скобка открывается один плюс три скобка закрывается'))
except Exception:
    print('Скорее всего, введены некорректные данные.')
