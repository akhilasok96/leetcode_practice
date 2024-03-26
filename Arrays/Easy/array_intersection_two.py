
# Each element in the result must be unique in resulting array
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        res = []
        for x in nums2:
            if x in seen:
                res.append(x)
                seen.remove(x)
        
        return res

nums1 = [1, 2, 2, 1]
nums2 = [2,2]

sol = Solution()
print(sol.intersect(nums1, nums2))
