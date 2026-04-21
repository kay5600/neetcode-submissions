class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length):
            num2 = target - nums[i]
            for j in range(i+1, length):
                if(num2 == nums[j]):
                    return [i,j]