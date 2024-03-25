class Solution:
    def reverseString(self, s: list[str]) -> None:
        def reverse(l,r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)
        reverse(0, len(s) - 1)
        return s

s = ["k","i","p","l","o"]
sol = Solution()
print(sol.reverseString(s))

# O(n) time complexity