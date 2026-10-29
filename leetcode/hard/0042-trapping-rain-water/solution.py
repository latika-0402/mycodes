class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            if left_max<right_max:
                water_trapped+=left_max-height[left]
                left+=1
            else:
                water_trapped+=right_max-height[right]
                right-=1
        return water_trapped

        
        