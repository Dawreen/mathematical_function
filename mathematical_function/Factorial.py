import math
from mathematical_function.MathFun import math_fun


class factorial(math_fun):
    def run(n):
        if n == 0: return 1
        res = 1
        for i in range(1, n+1):
            res = i * res
        return res

    def run_rec(n):
        if n == 0: return 1
        return n * factorial.run_rec(n-1)

    def exec(n: int) -> int:
        return factorial.run_rec(n)
    
    # TODO
    def print(self) -> tuple:
        return super().print()
    
    # TODO
    def graph(self):
        return super().graph()