class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for v, i in enumerate(nums):
            dupli = nums.copy()
            dupli.remove(i)
            for w, j in enumerate(dupli):
                if i + j == target:
                    return [v, w+1]
