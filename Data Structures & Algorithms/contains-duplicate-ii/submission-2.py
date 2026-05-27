'''You are given an integer array nums and an integer k
len(nums) large
nums[i] large and can be negative
k can be large

if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k, return true 

otherwise return false

Using an array of ints, check if there are 2 indices that have the same value
in the array and are less than or equal to k if subtracted from each other



if i is 0 then j is less than k
since i and j are distinct, k cannot be 0
start with i = 0 and j = 1

create a dictionary valueholder with nums[i] as the key and i as the value

while j is less than len(nums):
    check if nums[j] is in valueholder
    if valid:
        return true
    if not valid:
        add nums[j] into valueholder
        check if i - j == k:
            if valid:
                remove nums[i] from valueholder
                increment i by 1
            increment j by 1
return false
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) < 2: return False
        i, j = 0, 1
        valueholder = {nums[i]}
        while j < len(nums):
            if nums[j] in valueholder: return True
            valueholder.add(nums[j])
            if j - i == k:
                valueholder.remove(nums[i])
                i += 1
            j += 1

        return False