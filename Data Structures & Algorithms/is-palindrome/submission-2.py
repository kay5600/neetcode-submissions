class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.lower()
        l = 0 
        r = len(ls) - 1

        while l < r:
            while  not (self.alphaNum(ls[l])) and l<r:
                l+= 1
            while  not (self.alphaNum(ls[r])) and l<r:
                r -= 1
            if(ls[l] != ls[r]):
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self,c):
        return(ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')
        )
            