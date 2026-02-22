class Solution:
    def decodeString(self, s: str) -> str:
        str_st = []
        num_st = []
        num = ""
        for i in range(len(s)):
            if ("a" <= s[i] and s[i] <= "z") or s[i] == "[":
                str_st.append(s[i])
                if num:
                    num_st.append(num)
                num = ""

            if "0" <= s[i] and s[i] <= "9":
                num += s[i]

            temp_str = ""
            while s[i] == "]" and str_st[-1] != "[":
                poped = str_st.pop()
                temp_str = poped + temp_str

            if temp_str:
                str_st.pop()
                num_pop = num_st.pop()
                t = temp_str
                for i in range(int(num_pop) - 1):
                    temp_str = temp_str + t
                str_st.append(temp_str)

        return "".join(str_st)


print(Solution().decodeString("axb3[z]4[c]"))
print(Solution().decodeString("2[a3[b]]c"))
print(Solution().decodeString("ab2[c]3[d]1[x]"))
print(Solution().decodeString("10[a]"))
