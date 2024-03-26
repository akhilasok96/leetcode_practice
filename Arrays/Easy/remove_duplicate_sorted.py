class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        hmap = {}
        for x in nums:
            if x in hmap:
                hmap[x] = 1
            else:
                hmap[x] += 1
        return hmap
        