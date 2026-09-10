class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)

        for i,num in enumerate(nums):
            arr = [x * num if j != i else x for j, x in enumerate(arr)]
        return arr
            


        
            