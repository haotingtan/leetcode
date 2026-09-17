import string

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        current = []
        for num in digits:
            if not current:
                current += [c for c in phone[num]]
            else:
                new = []
                for c in phone[num]:
                    new += [cur+c for cur in current]
                current = new
        return current