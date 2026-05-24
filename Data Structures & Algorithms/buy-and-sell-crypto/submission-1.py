class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right, maxp, curr = left + 1, 0, 0
        while(right < len(prices)):
            curr = prices[right] - prices[left]
            maxp = max(maxp, curr)
            if prices[left] > prices[right]:
                left = right
            right += 1
        return maxp

            


