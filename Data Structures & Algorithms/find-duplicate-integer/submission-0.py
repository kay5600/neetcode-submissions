class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l ,r = 0, len(nums) - 1

        for l in range(len(nums)):
            while l < r:
                print(f"nums[l]   {nums[l]}     nums[r]  {nums[r]}")
                if nums[l] == nums[r]:
                    print(nums[l])
                    return nums[l]
                r = r - 1
            r = len(nums) -1
