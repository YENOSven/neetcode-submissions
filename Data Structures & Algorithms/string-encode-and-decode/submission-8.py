class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return "None"

        out = ""

        for s in strs:
            res = ""
            for letter in s:
                code = ord(letter)
                res += chr(code+1)
            out += res+" "
        
        out = out[:-1]

        return out
        

    def decode(self, s: str) -> List[str]:

        if s == "None":
            return []

        out = []

        lis = s.split(" ")

        for s in lis:
            res = ""
            for letter in s:
                code = ord(letter)
                res += chr(code-1)
            out.append(res)

        return out