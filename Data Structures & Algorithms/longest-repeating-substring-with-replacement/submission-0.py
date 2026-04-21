class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0
        maxf=0

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            maxf = max(maxf, count[s[i]])

            if (i-l + 1) - k > maxf:
                count[s[l]] -= 1
                l += 1
        return (i-l + 1)
