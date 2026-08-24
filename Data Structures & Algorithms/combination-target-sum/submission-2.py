'''
Make a list of lists holding combination of numbers that add to target
Numbers range from 2-30
Target can be any number between 2-30]
nums must have at least one item in it and a max of 20 values


lets use backtracking
loop through every number in nums
make a recursive function that takes target, currentsum, 

use collections Counter() to check for duplicates

nums[0] + nums[0]
nums[0] + nums[1]


'''
from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        returnList = []
        currsum = 0
        def bt(currsum: int, i: int, combo: List[int]):
            nonlocal returnList
            if (i >= len(nums)):
                return None

            currsum += nums[i]
            combo.append(nums[i])
            if (currsum == target):
                returnList.append(combo.copy())
                
            if (currsum < target):
                bt(currsum, i, combo)
            currsum -= nums[i]
            combo.pop()
            bt(currsum, i + 1, combo)
        
        bt(0, 0, [])
        unique_results = set(tuple(sorted(x)) for x in returnList)
        return [list(x) for x in unique_results]
