class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make an array of size 26 of 0's and use it as a 
        #key for the values to be stored
        #lower for caps
        dic = dict()
        
        for word in strs:
            myarray = [0]*26
            for let in word:
                myarray[ord(let.lower())-97] += 1
            if tuple(myarray) not in dic:
                dic[tuple(myarray)] = [word]
            else:
                dic[tuple(myarray)].append(word)
    

        return list(dic.values())


        
