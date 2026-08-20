import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num_list = []
        for i in range(len(tokens) - 1, -1, -1):
            stack.append(tokens[i])
        while (stack):
            if (self.is_number(stack[-1])):
                num_list.append(int(stack.pop()))
            else:
                operator = stack.pop()
                if (operator == "+"):
                    num_list[-2] = num_list[-2] + num_list[-1]
                    num_list.pop()
                if (operator == "-"):
                    num_list[-2] = num_list[-2] - num_list[-1]
                    num_list.pop()
                if (operator == "*"):
                    num_list[-2] = num_list[-2] * num_list[-1]
                    num_list.pop()
                if (operator == "/"):
                    if ((num_list[-2] < 0) ^ (num_list[-1] < 0)):
                        num_list[-2] = -(num_list[-2] // (-1 * num_list[-1]))
                    else:
                        num_list[-2] = num_list[-2] // num_list[-1]
                    
                    num_list.pop()
                
                    
        return num_list[0]
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False