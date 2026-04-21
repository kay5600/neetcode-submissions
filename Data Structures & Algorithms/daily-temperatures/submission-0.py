class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        count
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackind = stack.pop()
                res[stackind] = i - stackind
            stack.append((t,i))
        return res