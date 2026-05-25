class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {1 : 1, 2 : 2}
        return self.subaruStairs(n, mem)

    def subaruStairs(self, n: int, mem: dict) -> int:
        if n in mem: return mem[n]

        if (n > 1):
            mem[n] = self.subaruStairs(n - 1, mem) + self.subaruStairs(n - 2, mem)
            return mem[n]
        
