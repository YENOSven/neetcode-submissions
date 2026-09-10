class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = dict()
        dic2 = dict()

        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = 1
            else:
                dic1[s[i]] += 1
            if t[i] not in dic2:
                dic2[t[i]] = 1
            else:
                dic2[t[i]] += 1
        
        return dic1 == dic2

        