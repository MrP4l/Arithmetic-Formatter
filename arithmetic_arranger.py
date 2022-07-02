def arithmetic_arranger(problems, check=False):
    # Empty lists
    FirstsList = []
    SecondsList = []
    LinesList = []
    SolutionsList = []

    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Operands and operators splitted
    for problem in problems:
        problem_splitted = problem.split()
        fir = problem_splitted[0]
        ope = problem_splitted[1]
        sec = problem_splitted[2]

        if len(fir) > 4 or len(sec) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not fir.isnumeric() or not sec.isnumeric():
            return "Error: Numbers must only contain digits."

        if ope == '+' or ope == '-':
            if ope == "+":
                sol = str(int(fir) + int(sec))
            else:
                sol = str(int(fir) - int(sec))

            length = max(len(fir), len(sec)) + 2

            top = str(fir).rjust(length)
            bottom = ope + str(sec).rjust(length - 1)
            line = ''
            res = str(sol).rjust(length)

            for s in range(length):
                line += '-'
        else:
            return "Error: Operator must be '+' or '-'."
        # Appending to the lists
        FirstsList.append(top)
        SecondsList.append(bottom)
        LinesList.append(line)
        SolutionsList.append(res)

        firsts = '    '.join(FirstsList)
        seconds = '    '.join(SecondsList)
        lines = '    '.join(LinesList)
        solutions = '    '.join(SolutionsList)

    if check:
        arranged_problems = firsts + '\n' + seconds + '\n' + lines + '\n' + solutions
    else:
        arranged_problems = firsts + '\n' + seconds + '\n' + lines

    return arranged_problems
