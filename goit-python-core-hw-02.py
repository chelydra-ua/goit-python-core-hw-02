from symtable import Symbol


result = None
operand = None
operator = None
wait_for_number = True
symbol = input('Enter operand or operator ("=" for output): ')

while True:
    if symbol == '=':
        print(result)
        break
    elif symbol == '+' or '-' or '*' or '/':
        operator= symbol
        if operator == '+':
            result = result + operand
        elif operator == '-':
            result = result - operand
        elif operator == '*':
            result = result * operand
        elif operator == '/':
            result = result / operand
    else:
        operand = int(symbol)