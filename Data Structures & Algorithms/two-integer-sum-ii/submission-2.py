class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = 0

        l , r = 0, len(numbers) - 1

        while l < r:
            sumof = numbers[l] + numbers[r]
            if sumof == target:
                return [l + 1 ,  r + 1]
            elif sumof < target:
                l += 1 
            elif sumof > target:
                r -= 1

        