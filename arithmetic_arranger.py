def arithmetic_arranger(problems):
    x_line = ''
    y_line = ''
    divider_line = ''
    result_line = ''
    opperator = ''
    if len(problems) > 5:
        return 'Error: Too many problems'
    for problem in problems:
        if '-' not in problem and '+' not in problem:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if '-' in problem:
            problem = problem.split('-')
            opperator = '-'
        if '+' in problem: 
            problem = problem.split('+')
            opperator = '+'
        for num in problem:
            try: 
                num = int(num)
            except:
                return 'Error: Numbers must only contain digits.'
            if num > 9999:
                return 'Error: Numbers cannot be more than four digits.'
        x, y = problem
        if opperator == '-':
            result = x - y
        else: 
            result = x + y
        

        xlen = len(str(x))
        ylen = len(str(y))
        result_len = len(str(result))
        problem_width = 0
        problem_spacing = '    '
        
        if xlen > ylen:
            problem_width = xlen + 2
        else:
            problem_width = ylen + 2


        x_line += num_to_space(problem_width - xlen) + problem_spacing
        y_line += opperator + num_to_space(problem_width - ylen -1) + problem_spacing
        for i in range(1, problem_width):
            divider_line += '-'
        divider_line += problem_spacing
        result_line += num_to_space(problem_width - result_len) + result + problem_spacing

    return f'{x_line}\n{y_line}\n{divider_line}\n{result_line}'

def num_to_space(num):
    whitespace = ''
    for i in range(1, num):
        whitespace += ' '
    return whitespace
