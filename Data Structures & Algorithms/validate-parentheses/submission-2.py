class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.append(s[i])
            elif s[i] == "}" or s[i] == "]" or s[i] == ")":
                if not stack: return False
                stacktop = stack.pop()
                if s[i] == "}"and stacktop != "{":
                    return False
                if s[i] == "]"and stacktop != "[":
                    return False
                if s[i] == ")"and stacktop != "(":
                    return False
            else:
                return False
        if stack: return False
        return True