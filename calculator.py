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

    # if not num1.isdigit() or not  num1.isdigit():
    #     print('Those are not numbers!')
    #     continue
  
    
    if operator == '+':
        try:
            result = add(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    

    elif operator == '-':
        try:
            result = subtract(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        
    elif operator == '*':
        try:
            result = multiply(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
    elif operator == '/':
        try:
             result=divide(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
           
    elif operator == 'square':
        try:
              result=square(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
           
    elif operator == 'cube':
        try:
              result=cube(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
    elif operator == 'pow':
        try:
              result=power(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
    elif operator == 'mod':
        try:
               result=mod(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
           
    elif operator == 'x+':
        try:
            result=madd_mult(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
          
    elif operator == 'cubes':
        git committry:
            result=add_cubes(float(num1),float(num2))
           # break  
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
        
    else:
        result ="Please enter an operator with two integers"

    print(result)

#str.lstrip('-').isdigit()

