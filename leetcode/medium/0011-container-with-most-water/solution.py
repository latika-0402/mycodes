class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_result=0
        l=0
        r=len(height)-1
        while l<r:
            w=r-l
            current_height = min(height[l], height[r])
            current_area = w * current_height
            max_result=max(max_result,current_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_result

        