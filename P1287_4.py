def evaluate_expr(expr):
    def parse_number(expr):
        nonlocal index
        start = index
        while index < len(expr) and expr[index].isdigit():
            index += 1
        return int(expr[start:index])

    def parse_term(expr):
        nonlocal index
        left = parse_factor(expr)
        while index < len(expr) and expr[index] in ('*', '/'):
            operator = expr[index]
            index += 1
            right = parse_factor(expr)
            if operator == '*':
                left *= right
            else:
                left //= right

        return left

    def parse_factor(expr):
        nonlocal index
        if expr[index] == '(':
            index += 1
            result = parse_expr(expr)
            index += 1
            return result
        else:
            return parse_number(expr)

    def parse_expr(expr):
        nonlocal index
        left = parse_term(expr)
        while index < len(expr) and expr[index] in ('+', '-'):
            operator = expr[index]
            index += 1
            right = parse_term(expr)
            if operator == '+':
                left += right
            else:
                left -= right

        return left

    index = 0
    result = parse_expr(expr)
    if index < len(expr):
        print("ROCK")
        return None

    return result

expression = input()
result = evaluate_expr(expression)
if result is not None:
    print(result)
