class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lis = defaultdict(int)

        for i,num in enumerate(numbers):
            if target-num in numbers and target-num != num:
                lis[i] = num
        first_key = next(iter(lis))
        second_key = list(lis.keys())[1]

        return [first_key+1, second_key+1]