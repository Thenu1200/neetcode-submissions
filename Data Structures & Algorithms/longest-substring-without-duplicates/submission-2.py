class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right, maxlength, curr, seen = 0, 0, 0, set()

        while (right < len(s)):
            while (s[right] in seen):
                seen.discard(s[left])
                left += 1
            seen.add(s[right])
            print(seen)
            curr = len(seen)
            maxlength = max(curr, maxlength)
            right += 1
        
        return maxlength
                

        

        