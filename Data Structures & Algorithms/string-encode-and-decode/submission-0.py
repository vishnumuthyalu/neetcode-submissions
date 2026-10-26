class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for word in strs:
            encoded_list.append(str(len(word)))
            encoded_list.append("#")
            encoded_list.append(word)
        return "".join(encoded_list)
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end    
        return res    
        
