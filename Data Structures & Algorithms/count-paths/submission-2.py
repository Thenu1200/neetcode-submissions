class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {(1, 2) : 1, (2, 1) : 1, (1, 1) : 1}
        return self.paths(m, n, mem)

    def paths(self, m: int, n: int, mem: dict) -> int:
        if ((m, n) in mem): return mem[(m, n)]
        down, right = 0, 0
        if (m > 1):
            down = self.paths(m - 1, n, mem)
        if (n > 1):
            right = self.paths(m, n - 1, mem)
        mem[(m, n)] = down + right
        return mem[(m, n)]