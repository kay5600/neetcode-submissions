class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            element1 = l + ((r-l)//2)
            if nums[element1] == target:
                return element1
            elif nums[element1] > target:
                r = element1 -1
            elif nums[element1] < target:
                l = element1 + 1
        return -1
            