print('\nCALCULATOR\n')
print('Here is the list of all operations\n')
list = 'Addition, ' + 'Subtraction, ' + 'Multiplication ' + 'and Division'
print(list)

# to use "if" function you have to make valuable first
#in this case operation is our valuable


operation = input("\nType a first letter of the operation you want to perform or 'c' to cancel: ")


if operation == 'a':
    first = input('fist digit ')
    second = input('second digit ')
    summation = float(first) + float(second)
    print("sum is " + str(summation))
    print('\nThanks for using the calculator \n' + 'Restart the calculator to perform any opperation')

elif operation == 's':
    first = input('fist digit ')
    second = input('second digit ')
    subtraction = float(first) - float(second)
    print("difference is " + str(subtraction))
    print('\nThanks for using the calculator \n' + 'Restart the calculator to perform any opperation')

elif operation == 'm':
    first = input('fist digit ')
    second = input('second digit ')
    multiplication = float(first) * float(second)
    print("product is " + str(multiplication))
    print('\nThanks for using the calculator \n' + 'Restart the calculator to perform any opperation')

elif operation == 'd':
    first = input('fist digit ')
    second = input('second digit ')
    division = float(first) / float(second)
    print("division is " + str(division))
    print('\nThanks for using the calculator \n' + 'Restart the calculator to perform any opperation')

elif operation == 'c':
    print('\nThanks for using the calculator \n' + 'Restart the calculator to perform any opperation')

else :
    print('Error')