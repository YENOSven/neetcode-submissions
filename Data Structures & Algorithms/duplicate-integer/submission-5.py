class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis = set()

        for i in range(1, len(nums)+1):
            lis.add(nums[i-1])
            if len(lis) < i:
                return True
        return False