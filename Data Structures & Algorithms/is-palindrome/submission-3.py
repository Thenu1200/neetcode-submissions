class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = s.lower()
        new_s = "".join(filter(str.isalnum, new_s))

        start = 0
        end = len(new_s) - 1

        if len(new_s) == 0:
            return True
    
        while(start <= end):
            while (new_s[start] != new_s[end]):
                if(new_s[start].isalnum() and new_s[end].isalnum()):
                    print(new_s[start])
                    print(new_s[end])
                    return False
                if(not (new_s[start].isalnum())):
                    start += 1
                if(not new_s[end].isalnum()):
                    end -= 1
            end -= 1
            start += 1
        return True
        