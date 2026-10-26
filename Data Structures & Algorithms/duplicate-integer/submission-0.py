from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        counter = Counter(nums)

        for element in counter:
            if counter[element] > 1:
                return True
                break
        return False


        