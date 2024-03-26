class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        return hash
        
sol = Solution()
print(sol.removeDuplicates([1,2,2,3,4,4,5,5,6]))