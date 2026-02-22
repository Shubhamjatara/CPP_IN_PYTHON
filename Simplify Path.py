class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        temp_str = ""
        path += "/"
        for i in range(len(path)):
            if (
                "a" <= path[i]
                and path[i] <= "z"
                or "A" <= path[i]
                and path[i] <= "Z"
                or path[i] == "."
                or path[i] == "_"
                or "0" <= path[i]
                and path[i] <= "9"
            ):
                temp_str += path[i]

            if path[i] == "/" and temp_str:
                st.append(temp_str)
                temp_str = ""

            if st and st[-1] == ".":
                st.pop()
                st.pop()

            if st and st[-1] == "..":
                for i in range(3):
                    if st:
                        st.pop()

            if path[i] == "/" and st and st[-1] != "/" or len(st) == 0:
                st.append("/")

        if len(st) > 1 and st[-1] == "/":
            st.pop()
        if len(st) == 0:
            st.append("/")

        return "".join(st)


print(Solution().simplifyPath("/neetcode/practice//...///../courses"))
print(Solution().simplifyPath("/..//"))
print(Solution().simplifyPath("/..//_home/a/b/..///"))
print(Solution().simplifyPath("/a/../.././../../."))
print(Solution().simplifyPath("/../../../../../a"))
print(Solution().simplifyPath("/a/./b/./c/./d/"))
print(Solution().simplifyPath("/a/./b/../../c/"))
print(Solution().simplifyPath("/a/.."))
