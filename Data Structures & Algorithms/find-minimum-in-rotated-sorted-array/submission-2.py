class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i + 1 in range(len(nums)):

                if nums[i+1] < nums[i]:
                    return nums[i+1]
        return nums[0]