class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, number in enumerate(nums):
            need = target - number
            if need in seen:
                return [seen[need], index]
            seen[number] = index
        