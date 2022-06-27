class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for exp in s:
            if exp in '({[':
                stack.append(exp)
            
            elif not stack and exp in ')}]':
                return False
            else:
                top = stack.pop()
                if (top == '(' and exp != ')' or top == '{' and exp !='}' or top == '[' and exp!=']'):
                    return False
        return True if not stack else False
                
            
            
                
        
        