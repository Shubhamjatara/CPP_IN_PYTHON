class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ops = k
        stack = []
        temp_str = []

        for i in range(len(num)):
            while stack and ops > 0 and num[i] < stack[-1]:
                stack.pop()
                ops = ops - 1

            stack.append(num[i])

        while stack and ops > 0:
            stack.pop()
            ops = ops - 1

        while stack:
            temp_str.append(stack.pop())

        while temp_str and temp_str[-1] == "0":
            temp_str.pop()

        temp_str.reverse()
        ans = "".join(temp_str)
        return ans if ans else "0"


print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("10200", 1))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("4325043", 3))
print(Solution().removeKdigits("765028321", 5))
print(Solution().removeKdigits("10", 1))
