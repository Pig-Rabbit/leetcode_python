class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        out = []
        i = 0
        while i < len(nums)-2:
            l = i+1
            r = len(nums)-1
            if i != 0 and nums[i-1] == nums[i]:
                i += 1
            else:
                while l != r:
                    if nums[l] + nums[r] == -nums[i]:
                        out.append([nums[i],nums[l],nums[r]])
                        while l+1 != r and nums[l] == nums[l+1]:
                            l += 1
                        while r-1 != l and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                    elif nums[l] + nums[r] > -nums[i]:
                        r -= 1
                    else:
                        l += 1
                i += 1
        return out
            
                
