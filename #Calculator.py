#Calculator

print("This calculator operates in the form of a operation b. For instance, a/b or a*b")
print("the equation a mod b requires b to be an integer")
while True:
    a = float(input("Choose your first number: "))
    b = float(input("Choose your second number: "))
    
    operation = input("Choose from +, -, *, /, // (integer division) mod: ")
    if operation == 'mod':
        b = int(b)
    while b == 0 and operation == '/':
        print("division by 0 error: ")
        b = input("Choose a new number, not including 0: ")
    while b < 1 and operation == 'mod':
        print('a' + " mod " + 'b' + " is undefined : ")
        b = input("Choose a new number, not including 0: ")
    if operation == '+':
        print(float(a)+float(b))
        choice = input("Would you like to quit? Type Y or N: ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please type, Y or N: ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            continue
    elif operation == '-':
        print(float(a)-float(b))
        choice = input("Would you like to quit? Type Y or N: ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please type, Y or N: ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            continue
    elif operation == '*':
        print(float(a)*float(b))
        choice = input("Would you like to quit? Type Y or N: ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please type, Y or N: ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            continue
    elif operation == '/':
        print(float(a)/float(b))
        choice = input("Would you like to quit? Type Y or N: ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please type, Y or N: ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            continue
    elif operation == '//':
        print(float(a)//float(b))
        choice = input("Would you like to quit? Type Y or N: ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please type, Y or N: ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            continue
    elif operation == 'mod':
        print(float(a % b))
        choice = input("Would you like to quit? Type Y or N: ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please type, Y or N: ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            continue