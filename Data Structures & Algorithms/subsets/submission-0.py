'''
Find every combination of integers in the array
No duplicates per combination
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnlist = []
        currset = []

        def dfs(i):
            if i >= len(nums):
                returnlist.append(currset.copy())
                return
            currset.append(nums[i])
            dfs(i + 1)
            currset.pop()
            dfs(i + 1)

        dfs(0)
        return returnlist
        
            
        