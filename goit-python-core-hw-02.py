result = 0
operand = None
operator = '+'
wait_for_number = True

while True:
    elem = input('Enter operand or operator ("=" for output): ')
    if elem == '=':
        print(result)
        break
    elif elem == '+' or elem == '-' or elem == '*' or elem == '/':
        operator = elem
    else:
        operand = int(elem)
        if operator == '+':
            result = result + operand
        elif operator == '-':
            result = result - operand
        elif operator == '*':
            result = result * operand
        elif operator == '/':
            result = result / operand
