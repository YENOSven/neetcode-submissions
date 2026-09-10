class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i, string in enumerate(strs):
            key = tuple(sorted(string))

            if key not in res:
                res[key] = [string]
            else:
                res[key].append(string)

        return list(res.values())