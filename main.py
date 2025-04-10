def arithmetic_arranger(problems, show_answers=False):
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""

    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    final_string = ''

    for index, problem in enumerate(problems):
        tmp_list = problem.split(" ")

        # Check if it's addition or subtraction
        if tmp_list[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain digits only
        if not tmp_list[0].isdigit() or not tmp_list[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Check if numbers are not too long
        if len(tmp_list[0]) > 4 or len(tmp_list[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        op1 = int(tmp_list[0])
        op2 = int(tmp_list[2])
        operator = tmp_list[1]

        # Perform the operation
        if operator == '+':
            result = op1 + op2
        else:
            result = op1 - op2

        # Count spaces
        if len(tmp_list[0]) > len(tmp_list[2]):
            spaces2 = len(tmp_list[0]) - len(tmp_list[2])
            spaces1 = 2
        elif len(tmp_list[0]) < len(tmp_list[2]):
            spaces1 = len(tmp_list[2]) - len(tmp_list[0]) + 2
            spaces2 = 1
        else:
            spaces1 = 2
            spaces2 = 1

        # Count dashes
        dash_count = max(len(tmp_list[0]), len(tmp_list[2])) + 2
        spaces_result = dash_count - len(str(result))

        # Build the final string
        if index == 0:
            first_line += " " * spaces1 + tmp_list[0]
            second_line += operator + " " * spaces2 + tmp_list[2]
            dash_line += "-" * dash_count
            result_line += " " * spaces_result + str(result)
        else:
            first_line += " " * 4 + " " * spaces1 + tmp_list[0]
            second_line += " " * 4 + operator + " " * spaces2 + tmp_list[2]
            dash_line += " " * 4 + "-" * dash_count
            result_line += " " * 4 + " " * spaces_result + str(result)

    final_string = first_line + '\n' + second_line + '\n' + dash_line
    if show_answers:
        final_string += '\n' + result_line

    return final_string


# Example usage
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49", "9999 + 9999"], True)}')