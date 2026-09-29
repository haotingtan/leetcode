class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if not n or n == 0:
            return 0
        curr = ['(']
        while len(curr[0]) != 2*n:
            new = []
            for c in curr:
                left_count = c.count('(')
                right_count = c.count(')')
                if left_count > right_count:
                    new.append(c+')')
                if left_count < n:
                    new.append(c+'(')
            curr = new
        return (curr)

