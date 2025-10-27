"""
Solutions to module 2 - A calculator
Student: Marcus Steiner
Mail: marcus.steiner.3581@student.uu.se
Reviewed by: David Bagstevold
Reviewed date: 24-09-2024
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)
        
class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def fac(x):
    if x <= 0:
        raise EvaluationError(f'Factorial of a negative number was attempted: {x}')
    elif x%1 != 0:
        raise EvaluationError(f'Factorial of a non-whole number was attempted: {x}')
    return math.factorial(int(x))

def log(x):
    if x <= 0:
        raise EvaluationError(f'Logarithm of a negative number was attempted: {x}')
    return math.log(x)

def arglist(wtok, variables):
    result = []
    
    wtok.next()
    result.append(assignment(wtok, variables))
    while wtok.get_current() == ',':
        wtok.next()
        result.append(assignment(wtok, variables))
    wtok.next()

    return result

def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    
    if wtok.is_at_end():
        return result
    else:
        raise SyntaxError("Expected *EOL*")


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            var = wtok.get_current()
            variables[var] = result
            wtok.next()
        else:
            raise SyntaxError("Expected a name")
        
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        if wtok.get_previous() == '-':
            result = result - term(wtok, variables)
        
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        wtok.next()
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
        else:
            denominator = factor(wtok, variables)
            if denominator == 0:
                raise EvaluationError("Error, Division by zero")
            else:
                result = result / denominator
    
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    FUNCTIONS_1 = {'sin':math.sin, 'cos':math.cos, 'exp':math.exp, 'log':log, 'fac':fac, 'abs':abs}
    FUNCTIONS_N = {'sum':sum, 'max':max}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
        
    elif wtok.is_name():
        wtok.next()
        if wtok.get_previous() in FUNCTIONS_1.keys():
            if wtok.get_current() == '(':
                result = FUNCTIONS_1[wtok.get_previous()](arglist(wtok, variables)[0])
            else:
                raise SyntaxError("Expected '('")
        
        elif wtok.get_previous() in FUNCTIONS_N.keys():
            if wtok.get_current() == '(':
                result = FUNCTIONS_N[wtok.get_previous()](arglist(wtok, variables))
            else:
                raise SyntaxError("Expected '('")
        
        elif wtok.get_previous() in variables.keys():
            result = variables[wtok.get_previous()]
        
        elif wtok.get_previous() == 'vars':
            result = 'vars'
        
        else:
            raise EvaluationError(f"Undefined variable: {wtok.get_previous()}")
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
        
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number, name, function or '('")  
    
    return result


         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                if result == 'vars':
                    for key, value in variables.items():
                        print(f'{key}\t:\t{value}')
                else:
                    variables['ans'] = result
                    print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                if wtok.is_at_end():
                    print(
                    f"*** Error occurred at *EOL* just after '{wtok.get_previous()}'")
                else:
                    print(
                    f"*** Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
            
            except EvaluationError as ce:
                print("*** Error. ", ce)
 


if __name__ == "__main__":
    main()