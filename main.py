def arithmetic_arranger(problems, show_answers=False):
    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    final_string = ''
    for i in problems:
        op1 = 0
        op2 = 0
        result = 0
        tmp_list = i.split(" ")
        final = ''
        dashes = 0
        tmp_dashes = 0
        spaces1 = 0
        spaces2 = 0

        # Check if its addition or subtraction
        if tmp_list[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if it contains digits only
        if not tmp_list[0].isdigit() or not tmp_list[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        # Check if numbers are not too long
        if len(tmp_list[0]) > 4 or len(tmp_list[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        op1 = int(tmp_list[0])
        op2 = int(tmp_list[2])
        if tmp_list[1] == '+':
            result = op1 + op2
        else:
            result = op1 - op2

        # Counting spaces
        if len(tmp_list[0]) > len(tmp_list[2]):
            spaces2 = len(tmp_list[0]) - len(tmp_list[2])
        elif len(tmp_list[0]) < len(tmp_list[2]):
            spaces1 = len(tmp_list[2]) - len(tmp_list[0])
        spaces1 += 2
        spaces2 += 1

        # Counting dashes
        for j in i:
            tmp_dashes += 1
            if j == '+' or j == '-' or j == ' ':
                tmp_dashes = 0
            if tmp_dashes > dashes:
                dashes = tmp_dashes
        dashes += 2
        spacesR = dashes - len(str(result))

        # Building final string
        if problems.index(i) == 0:
            first_line += " " * spaces1 + tmp_list[0]
            second_line += tmp_list[1] + spaces2 * ' ' + tmp_list[2]
            dash_line += dashes * "-"
            result_line += spacesR * ' ' + str(result)
        else:
            first_line += " " * (spaces1 + 4) + tmp_list[0]
            second_line += 4 * ' ' + tmp_list[1] + spaces2 * ' ' + tmp_list[2]
            dash_line += 4 * ' ' + dashes * "-"
            result_line += 4 * ' ' + spacesR * ' ' + str(result)

    final_string = first_line + '\n' + second_line + '\n' + dash_line
    if (show_answers):
        final_string += '\n' + result_line
    return final_string


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49", "9999 + 9999"], True)}')