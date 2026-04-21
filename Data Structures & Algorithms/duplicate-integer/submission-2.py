class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setm = set()

        for i in nums:
            if i in setm:
                return True
            else:
                setm.add(i)
        return False
