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
        if wait_for_number == False:
            operator = elem
            wait_for_number = True
        else:
            print(f"elem {elem} is not a + or - or * or /")
    else:
        try:
            operand = int(elem)
            if wait_for_number == True:
                if operator == '+':
                    result = result + operand
                elif operator == '-':
                    result = result - operand
                elif operator == '*':
                    result = result * operand
                elif operator == '/':
                    result = result / operand
                wait_for_number = False
            else:
                print(f"elem {elem} is not a number")
        except ValueError:
            print(f"elem {operand} is not a number")
