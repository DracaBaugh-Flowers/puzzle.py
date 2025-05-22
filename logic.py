def eval_expr(expr, vars):
    # Simple safe evaluation (assumes expr like "A and not B")
    expr = expr.replace("and", "and").replace("or", "or").replace("not", "not")
    for var, val in vars.items():
        expr = expr.replace(var, str(val))
    return eval(expr)

# Example
if __name__ == "__main__":
    expr = "A and not B"
    vars = {"A": True, "B": False}
    result = eval_expr(expr, vars)
    print(f"Expression '{expr}' is {result}")
