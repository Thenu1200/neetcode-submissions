class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        i = 0 
        j = 0
        for n in range(len(nums)):
            difference = (target - nums[n])
            if (difference in dictionary):
                if (dictionary[difference] > n):
                    i = n
                    j = dictionary[difference]
                else:
                    j = n
                    i = dictionary[difference]
                break
            dictionary[nums[n]] = n

        return [i, j]