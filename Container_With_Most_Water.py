class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        while left != right:
            if height[left] >= height[right]:
                if (right-left)*height[right] > max_area:
                    max_area = (right-left)*height[right]
                right -= 1
            else:
                if (right-left)*height[left] > max_area:
                    max_area = (right-left)*height[left]
                left += 1
        return max_area
            
