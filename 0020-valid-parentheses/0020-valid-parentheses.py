class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i not in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                top =stack.pop()
                if top !=pairs[i]:
                    return False

        return len(stack)==0
        