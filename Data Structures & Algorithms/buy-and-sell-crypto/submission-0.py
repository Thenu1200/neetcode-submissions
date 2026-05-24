class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        left, right, maxp, curr = 0, 1, 0, 0
        while(right < len(prices)):
            curr = prices[right] - prices[left]
            maxp = max(maxp, curr)
            if prices[left] > prices[right]:
                left = right
            right += 1
        return maxp

            


