class Solution:
    def reverseBits(self, n: int) -> int:
        number_of_times = 0
        cur_n = n
        rev_num = 0
        for digit in range(32)[::-1]:
            cur = 2**digit
            if cur_n >= cur:
                cur_n -= cur
                rev_num += 2** (31-digit)
            if cur_n == 0:
                break
        return rev_num