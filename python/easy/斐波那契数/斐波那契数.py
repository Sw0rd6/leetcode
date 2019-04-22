class Solution:
    def fib(self, N: int) -> int:
        fib = [0, 1]
        if N < 2:
            return fib[N]
        else:
            for i in range(2, N+1):
                tmp = fib[0] + fib[1]
                fib[0] = fib[1]
                fib[1] = tmp
        return fib[1]
