class Solution:
    def reverseString(self, s: list[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1 
        return s

s = ["a","x","k","b","f"]
sol = Solution()
print(sol.reverseString(s))

# O(n) time complexity