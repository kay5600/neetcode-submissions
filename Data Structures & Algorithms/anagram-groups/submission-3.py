class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:

            count = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        result = []

        for group in groups:
            result.append(groups[group])
        
        return result
