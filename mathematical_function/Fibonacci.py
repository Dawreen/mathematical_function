import math
from mathematical_function.MathFun import math_fun


class fibonacci(math_fun):
    def run_rec(n: int) -> int:
        if n in {0, 1}:  # Base case
            return n
        return fibonacci.run_rec(n - 1) + fibonacci.run_rec(n - 2)  # Recursive case
    
    def run(n: int) -> int:
        if n in {0, 1}:
            return n
        else:
            i1 = 0
            i2 = 1
            res = 0
            for i in range(n-1):
                res = i1 + i2
                i1 = i2
                i2 = res
            return res
        
    def run_fast(n):
        return round(1/math.sqrt(5) * pow(((1 + math.sqrt(5))/2), n) - 1/math.sqrt(5) * pow(((1 - math.sqrt(5))/2), n))

    def exec(n: int) -> int:
        return fibonacci.run(n)
    
    # TODO
    def print(self) -> tuple:
        return super().print()
    
    # TODO
    def graph(self):
        return super().graph()
