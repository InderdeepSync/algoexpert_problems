class Solution:

    def my_eval(self, s: str):
        result = 0
        flag = 1

        s += '+'
        num = 0
        for i in range(0, len(s)):
            ch = s[i]
            if ch in ('+', '-'):
                result += flag * int(num)

                num = 0
                flag = 1 if ch == '+' else -1
            else:
                num = num * 10 + int(ch)

        return result

    def calculate(self, s: str) -> int:
        stack = []

        for ch in s:
            if ch == ' ':
                continue
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                expression = stack.pop() + ch
                res = str(self.my_eval(expression[1: -1]))
                if stack:
                    if stack[-1][-1] == '+' and res[0] == '-':
                        stack[-1] = stack[-1][:-1] + res
                    elif stack[-1][-1] == '-' and res[0] == '-':
                        stack[-1] = stack[-1][:-1] + '+' + res[1:]
                    else:
                        stack[-1] += res
                else:
                    stack.append(res)
            else:  # isNum, '+', '-'
                if stack:
                    stack[-1] += ch
                else:
                    stack.append(ch)

        return self.my_eval(stack[-1])


if __name__ == '__main__':
    print(Solution().calculate("-2+ 1"))
