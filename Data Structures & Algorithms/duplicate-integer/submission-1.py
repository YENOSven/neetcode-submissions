class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x = None
        for i in nums:
            if i == x:
                return True
            else:
                x = i
        return False