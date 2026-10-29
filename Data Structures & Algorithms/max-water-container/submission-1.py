class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_amount = 0

        while start<end:
            
            max_amount = max(max_amount, (end - start) * min(heights[start], heights[end]))
            
            if heights[start] < heights[end]:
                start = start + 1
            else:
                end = end - 1

        return max_amount


        