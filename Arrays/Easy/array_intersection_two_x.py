
# Each element in the result must be unique in resulting array
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hmap = {}
        res = []
        for x in nums1:
            if x not in hmap:
                hmap[x] = 1
            elif x in hmap:
                hmap[x] += 1
        
        for x in nums2:
            if x in hmap and hmap[x] >= 1:
                res.append(x)
                hmap[x] -= 1
        
        return res

nums1 = [1, 2, 2, 1]
nums2 = [2,2]

sol = Solution()
print(sol.intersect(nums1, nums2))