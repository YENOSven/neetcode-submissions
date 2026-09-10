class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = dict()
        dic2 = dict()

        for el in s:
            if el not in dic1:
                dic1[el] = 1
            else:
                dic1[el] += 1

        for el in t:
            if el not in dic2:
                dic2[el] = 1
            else:
                dic2[el] += 1

        return dic1 == dic2

            