# arithmetic_formatter
## freecodecamp challenge: arithmetic formatter
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

```  
235
+  52
-----
```
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

### Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

```   
32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

```  
32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

### Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
### Development
Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.

### Testing
The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.


## Notes about my solution

This is my second attempted sollution to this challenge, because for my first attempt I failed to get the errors to work properly, because i was using multiple seperate function within the main function to achieve the desired functionallity, I couldn't use `return` to break out of the loop when an error occoured. See old solution below: 

### My final solution 
Beucase of my earlier attempt failing due to the fact I couldn't exit the loop in case of an error I decided to put all the funtionallity in one loop, which turned out not to be a bad solution since I also managed to optimise the solution to the point it has less than 100 lines total. 

```
def arithmetic_arranger(problems):
    problem_spacing = '    '
    first_line = ''
    second_line = ''
    divider_line = ''
    result_line = ''
    for problem in problems: 
        if len(problems) > 5:
            print('Error: Too many problems.')
        if '+' not in problem and '-' not in problem:
            print("Error: Operator must be '+' or '-'.")
        if '+' in problem:
            problem = function(problem, '+')
        else: 
            problem = function(problem, '-')
        
        if error != 'false': 
            break

        # find problem width
        first_len = len(str(problem[0]))
        second_len = len(str(problem[1]))
        result_len = len(str(problem[2]))
        problem_width = 0
        if first_len > second_len:
            problem_width = first_len + 2
        else:
            problem_width = second_len + 2
        
        # format first line
        first_line += num_to_whitespace(problem_width - first_len) + str(problem[0]) + problem_spacing
        
        # format second line
        second_line += num_to_whitespace(problem_width - second_len) + str(problem[1]) + problem_spacing

        # format divider line
        for i in range(1, problem_width):
            divider_line += '-'
        divider_line += problem_spacing

        # format result line
        result_line += num_to_whitespace(problem_width - result_len) + str(problem[2]) + problem_spacing
        return f'{first_line}\n{second_line}\n{divider_line}\n{result_line}'

def function(problem, opperator):
    problem = problem.split(opperator)
    first, second = problem
    first = int(first)
    global error 
    errors(first)
    second = int(second)
    errors(second)
    if opperator == '+':
        result = first + second
    else:
        result = first - second
    return [first, second, result]

def num_to_whitespace(value):
    whitespace = ''
    for i in range(1, value):
        whitespace += ' '
    return whitespace

def errors(num):
    if type(num) != int:
        print('Error: Numbers must only contain digits.')
    elif num > 4:
        print('Error: Numbers cannot be more than four digits.')

print(arithmetic_arranger(["43322 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

```