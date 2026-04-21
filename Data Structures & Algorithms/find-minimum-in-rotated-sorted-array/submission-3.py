class Solution:
    def findMin(self, nums: List[int]) -> int:
        s , e = 0 , len(nums)-1
        curr_min = nums[0]

        while s < e:
            mid = s + (e-s)//2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid - 1
        return min(curr_min, nums[s])