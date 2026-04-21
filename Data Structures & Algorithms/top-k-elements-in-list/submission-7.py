class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         count = {}


         for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

         countlist = []

         for i, cnt in count.items():
            countlist.append([cnt, i])
         countlist.sort()

         res = []

         while len(res) < k:
            res.append(countlist.pop()[1])
        
         return res
        