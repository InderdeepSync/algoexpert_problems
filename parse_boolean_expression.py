from functools import reduce

class Solution(object):

    def eval(self, expression):
        result = None
        temp = expression[2:-1].split(',')

        if expression[0] == '!':
            result = not self.VALUES[temp[0]]
        elif expression[0] == '&':
            result = all(map(lambda t: self.VALUES[t], temp))
        elif expression[0] == '|':
            result = any(map(lambda t: self.VALUES[t], temp))

        return 't' if result else 'f'


    def parseBoolExpr(self, expression): #1106 Verified on Leetcode
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        self.VALUES = {'t': True, 'f': False}

        for ch in expression:
            if not stack and ch in ('t', 'f'):
                return self.VALUES[ch]

            if ch in ('!', '&', '|'):
                stack.append(ch)
            elif ch in ('(', 't', 'f', ','):
                stack[-1] +=  ch
            elif ch == ')':
                res = self.eval(stack.pop() + ch)
                if stack:
                    stack[-1] += res
                else:
                    stack.append(res)

        return True if stack[-1] == 't' else False

if __name__ == '__main__':
    print(Solution().parseBoolExpr("f"))


