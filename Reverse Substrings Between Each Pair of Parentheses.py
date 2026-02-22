class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            temp = []
            if s[i] == ")":
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())

                stack.pop()

            if temp:
                for t in temp:
                    stack.append(t)

            if s[i] != ")":
                stack.append(s[i])

        return "".join(map(str, stack))


print(Solution().reverseParentheses("(abcd)"))
print(Solution().reverseParentheses("(u(love)i)"))
print(Solution().reverseParentheses("(ed(et(oc))el)"))
