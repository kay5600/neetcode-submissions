class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set()

        for i in nums:
            print(i)
            if i in sets:
                return True
            sets.add(i)
        return False