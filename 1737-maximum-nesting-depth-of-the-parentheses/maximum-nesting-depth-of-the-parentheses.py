class Solution:
    def maxDepth(self, s: str) -> int:
        max_lvl = 0
        lvl = 0
        for v in s:
            if v == '(':
                lvl += 1
            elif v == ')':
                if max_lvl < lvl:
                    max_lvl = lvl
                lvl -= 1
        
        return max_lvl