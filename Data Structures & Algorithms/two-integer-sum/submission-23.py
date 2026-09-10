class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    d.append(i)
                    d.append(j)
                    return d
        return d
            