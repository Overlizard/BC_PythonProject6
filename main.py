# Create my function to convert celsius to fahrenheit
def c_to_f(c_value):
    converted_f = float((9/5) * (c_value + 32))
    return converted_f


# Create my function to convert fahrenheit to celsius
def f_to_c(f_value):
    converted_c = float((5/9) * (f_value - 32))
    return converted_c


# Gather input from user and turn to a list to grab type and temp
type_and_temp = input('Menu:\n'
                      'Enter in the form of \'option temp\'\n'
                      '1: Convert from Fahrenheit to Celsius\n'
                      '2: Convert from Celsius to Fahrenheit\n'
                      '\'quit\' to exit program\n').split()


# Begin the loop after the first menu selection
while type_and_temp[0] != 'quit':
    try:
        type_and_temp[1] = int(type_and_temp[1])
        if type_and_temp[0] == '1':
            print(f'Fahrenheit converted to Celsius is: {f_to_c(type_and_temp[1]):.2f}\n')
        elif type_and_temp[0] == '2':
            print(f'Celsius converted to Fahrenheit is: {c_to_f(type_and_temp[1]):.2f}\n')

# Exception handling for both the index error if the user entered incorrectly and
    # Value Error for if the unit was not entered as a number
    except IndexError:
        print('\nReenter menu options\n'
              '\'option temperature\'\n')
    except ValueError:
        print('Invalid temperature value')

    type_and_temp = input('enter new values or enter \'quit\' to quit:\n').split()
    if type_and_temp == 'quit':
        print('Exiting program')
