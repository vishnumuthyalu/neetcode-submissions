class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            new_label = "".join(sorted(word))
            if new_label not in groups:
                groups[new_label] =[]
            groups[new_label].append(word)
        
        return list(groups.values())
        