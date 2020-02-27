def expressionValue(x, operand, y):
    if operand == "+":
        return x + y
    elif operand == "-":
        return x - y
    elif operand == "*":
        return x * y
    elif operand == "//":
        return x // y
    elif operand == "/":
        return x / y
    elif operand == "%":
        return x % y
    elif operand == "**":
        return x ** y
    else:
        return "INVALID ARGUMENTS"


if __name__ == "__main__":
    x = float(input())
    operand = input()
    y = float(input())
    result = expressionValue(x, operand, y)
    if result != "INVALID ARGUMENTS":
        print(f"Resultat: {result}")

    else: print(result)
