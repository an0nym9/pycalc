import ast
import operator

from pycalc.utils.guards import Result, handle_exception, enhance_params
from pycalc.basic import sum, difference, product, qoutient
from pycalc.number import (
    is_prime, is_semi_prime, gen_primes, gen_semi_primes,
    fraction_to_decimal, decimal_to_fraction, factor, lcm, gcd, remain,
)
from pycalc.probability import factorial, permutations, combinations

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.Pow: operator.pow,
}

FUNCTIONS = {
    # Basic
    "sum": sum,
    "difference": difference,
    "product": product,
    "qoutient": qoutient,

    # Number
    "is_prime": is_prime,
    "is_semi_prime": is_semi_prime,
    "gen_primes": gen_primes,
    "gen_semi_primes": gen_semi_primes,
    "fraction_to_decimal": fraction_to_decimal,
    "decimal_to_fraction": decimal_to_fraction,
    "factor": factor,
    "lcm": lcm,
    "gcd": gcd,
    "remain": remain,

    # Probability
    "factorial": factorial,
    "permutations": permutations,
    "combinations": combinations,
}

@handle_exception
@enhance_params
def eval_expr(node: ast.AST) -> any:
    """Evaluate expressions"""
    if isinstance(node, ast.BinOp):
        left = eval_expr(node.left)
        right = eval_expr(node.right)
        if isinstance(left, Result):
            if not left.is_ok():
                raise ValueError(f"Left operand failed: {left.err()}")
            left = left.unwrap()
        if isinstance(right, Result):
            if not right.is_ok():
                raise ValueError(f"Right operand failed: {right.err()}")
            right = right.unwrap()
        op_type = type(node.op)
        if op_type in OPERATORS:
            return OPERATORS[op_type](left, right)
        raise ValueError(f"Unsupported operator: {op_type}")
    elif isinstance(node, ast.Constant):
        return node.value
    elif hasattr(ast, "Num") and isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.UnaryOp):
        operand = eval_expr(node.operand)
        if isinstance(operand, Result):
            if not operand.is_ok():
                raise ValueError(f"Unary operand failed: {operand.err()}")
            operand = operand.unwrap()
        if isinstance(node.op, ast.UAdd):
            return +operand
        elif isinstance(node.op, ast.USub):
            return -operand
        raise ValueError(f"Unsupported unary operator: {type(node.op)}")
    elif isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Only named functions are allowed")
        func_name = node.func.id
        if func_name in FUNCTIONS:
            args = [eval_expr(arg).unwrap() for arg in node.args]
            kwargs = {kw.arg: eval_expr(kw.value).unwrap() for kw in node.keywords}
            res = FUNCTIONS[func_name](*args, **kwargs)
            if isinstance(res, Result):
                if not res.is_ok():
                    raise ValueError(f"Function {func_name} failed: {res.err()}")
                return res.unwrap()
            return res
        raise ValueError(f"Function {func_name} is not allowed")
    raise TypeError(f"Unsupported expression: {type(node)}")
