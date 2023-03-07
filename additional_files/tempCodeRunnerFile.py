x = sympy.symbols('x')
        y = sympy.symbols('y')
        z = sympy.symbols('z')
        k = sympy.symbols('k')

        expr = sympy.parse_expr(equation)
        result = sympy.solve(expr, [x, y,z,k])
        return re