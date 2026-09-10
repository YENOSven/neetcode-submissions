class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {0:0}
        
        for num in nums:
            if num not in dic:
                dic[num] = 1;
            else:
                dic[num] += 1;
        
        return sorted(dic, key=dic.get, reverse=True)[:k]
        

            