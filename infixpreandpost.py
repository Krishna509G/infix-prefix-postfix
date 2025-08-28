# Infix ↔ Prefix ↔ Postfix Conversion in Python

# Operator precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

# Infix to Postfix
def infix_to_postfix(expression):
    stack = []
    result = []
    for char in expression:
        if char.isalnum():  # Operand
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return "".join(result)

# Infix to Prefix
def infix_to_prefix(expression):
    # Reverse the expression
    expression = expression[::-1]
    # Swap brackets
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    postfix = infix_to_postfix(expression)
    return postfix[::-1]

# Postfix to Infix
def postfix_to_infix(postfix):
    stack = []
    for char in postfix:
        if char.isalnum():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a}{char}{b})")
    return stack[-1]

# Prefix to Infix
def prefix_to_infix(prefix):
    stack = []
    for char in prefix[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{char}{b})")
    return stack[-1]

# Postfix to Prefix
def postfix_to_prefix(postfix):
    stack = []
    for char in postfix:
        if char.isalnum():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(char + a + b)
    return stack[-1]

# Prefix to Postfix
def prefix_to_postfix(prefix):
    stack = []
    for char in prefix[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + char)
    return stack[-1]


if __name__ == "__main__":
    infix = "A*(B+C)/D"

    print("Infix Expression   :", infix)

    postfix = infix_to_postfix(infix)
    prefix = infix_to_prefix(infix)

    print("Postfix Expression :", postfix)
    print("Prefix Expression  :", prefix)

    # Checking reverse conversions
    print("Postfix → Infix    :", postfix_to_infix(postfix))
    print("Prefix  → Infix    :", prefix_to_infix(prefix))
    print("Postfix → Prefix   :", postfix_to_prefix(postfix))
    print("Prefix  → Postfix  :", prefix_to_postfix(prefix))
