class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        
        def operator(sign, num):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop()*num)
            else:
                temp_num = stack.pop()
                if temp_num < 0 and temp_num % num != 0 :
                    stack.append(temp_num//num+1)
                else:
                    stack.append(temp_num//num)
        
        index = 0
        sign = '+'
        num = 0
        while index < len(s):
            if s[index].isdigit():
                num = num*10 + int(s[index])
            elif s[index] in '+-*/':
                operator(sign, num)
                num = 0
                sign = s[index]
            index += 1
        
        operator(sign, num)
        return sum(stack)
