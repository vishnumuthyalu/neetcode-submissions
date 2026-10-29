class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i  + 1
            k = (len(nums) - 1)
            target = nums[i] * -1
         
            while j<k:
                if nums[j] + nums[k] > target:
                    k = k - 1
                elif nums[j] + nums[k] < target:
                    j = j + 1
                else: 
                    triplet = [nums[i], nums[j], nums[k]]
                    result.append(triplet)
                    j = j + 1 
                    k = k - 1 
                    while j<k and nums[j] == nums[j - 1]:
                        j = j+1
                    while j<k and nums[k] == nums[k + 1]:
                        k = k - 1  
                
        return result


        