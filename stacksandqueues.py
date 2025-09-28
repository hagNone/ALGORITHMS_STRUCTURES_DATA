class stack(object):
    # is valid parentheses
    def isValid(self, s):
        stack=[]
        mapping={")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping:
                top_element=stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    
    # evaluate reverse polish notation
    def evalRPN(self, tokens):
        stack=[]
        operators={"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()

                if token=='+':
                    stack.append(a+b)
                elif token=='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack.pop()
    
    #next greater element
    def nextgreater(self, nums1, nums2):
        stack=[]
        mapping={}

        for num in nums2:
            while stack and stack[-1]<num:
                mapping[stack.pop()]=num
            stack.append(num)
        
        return [mapping.get(num,-1) for num in nums1]