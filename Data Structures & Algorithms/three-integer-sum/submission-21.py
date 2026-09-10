class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        counts = Counter(nums) 

        #nums[i] + nums[j] = -nums[k]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = -(nums[i] + nums[j])
                if target in counts:
                    need = 1
                    if target == nums[i]:
                        need += 1
                    if target == nums[j]:
                        need += 1
                    if need <= counts[target]:
                        triple = sorted([nums[i], nums[j], target])
                        ans.add(tuple(triple))
                    if target == 0 and counts[0] > 2:
                        ans.add(tuple([0,0,0]))
            
        return list(ans)