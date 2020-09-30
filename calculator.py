"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    input_string= input('Enter your equation:')
    token = input_string.split(' ')
    if 'q' in token:
        print('The program will quit now')
        break
    if len(token) < 2:
        print('Not enough input')
        token = input_string.split(' ')
        continue
        
    operator=token[0]
    num1=token[1]
    num2=token[2]

    if len(token) > 3:
         num3 = tokens[3]
        
    result = None

    try:    
        if operator == '+':
            result = add(float(num1),float(num2))
        
        elif operator == '-':
            result = subtract(float(num1),float(num2))
         
        elif operator == '*':
            result = multiply(float(num1),float(num2))
                   
        elif operator == '/':
            result=divide(float(num1),float(num2))
                   
        elif operator == 'square':
            result=square(float(num1),float(num2))
                      
        elif operator == 'cube':
            result=cube(float(num1),float(num2))
         
        elif operator == 'pow':
            result=power(float(num1),float(num2))         
            
        elif operator == 'mod':
            result=mod(float(num1),float(num2))
           
           
        elif operator == 'x+':
            result=madd_mult(float(num1),float(num2))        
          
        elif operator == 'cubes':
             result=add_cubes(float(num1),float(num2))
                 
        else:
            result ="Please enter an operator with two integers"
         
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    print(result)



