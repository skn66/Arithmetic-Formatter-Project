def arithmetic_arranger(problems, display_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Initialize lists for each line of the formatted output
    first_line = []
    second_line = []
    dashes = []
    results = []

    # Process each problem
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if the numbers are valid
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Check if the numbers are too large
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the length of the formatted problem
        max_len = max(len(num1), len(num2)) + 2  # 2 spaces for the operator and one extra space
        first_line.append(num1.rjust(max_len))
        second_line.append(operator + num2.rjust(max_len - 1))
        dashes.append('-' * max_len)

        # Calculate the result if needed
        if display_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(max_len))

    # Join all lines with appropriate spacing
    arranged_problems = '    '.join(first_line) + '\n' + \
                        '    '.join(second_line) + '\n' + \
                        '    '.join(dashes)

    # Add results if requested
    if display_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) )
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))