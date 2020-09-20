def arithmetic_arranger(problems, calculate = False):

    lines = ['', '', '', '']
    tab = '    ' # 4 spaces
    arranged_problems = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        arr = problem.split()
        operand_1 = arr[0]
        operator = arr[1]
        operand_2 = arr[2]
        
        # check the length of the number, max 4 digits
        if (len(operand_1) > 4 or len(operand_2) > 4):
            return "Error: Numbers cannot be more than four digits."

        # check input must be digits
        if not operand_1.isnumeric() or not operand_2.isnumeric():
            return "Error: Numbers must only contain digits."

        if (operator not in ['+', '-']):
            return "Error: Operator must be '+' or '-'."

        # determine maximum length
        max_length = max(len(operand_1), len(operand_2)) + 2

        lines[0] += operand_1.rjust(max_length) + tab
        lines[1] += operator + operand_2.rjust(max_length - 1) + tab
        lines[2] += "".rjust(max_length, '-') + tab

        if (calculate):
            if operator == "+":
                result = str(int(operand_1) + int(operand_2))
            else:
                result = str(int(operand_1) - int(operand_2))
            lines[3] += result.rjust(max_length) + tab

    if (not calculate):
        # remove the last item (result)
        lines.pop()

    for line in lines:
        arranged_problems += line.rstrip() + '\n'

    # remove the last "\n" before returning
    return arranged_problems.rstrip("\n")