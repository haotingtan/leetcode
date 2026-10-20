
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeft(low, upper):
            if low > upper:
                return -1

            mid = low + (upper - low) // 2

            if nums[mid] == target:
                left = findLeft(low, mid - 1)
                return mid if left == -1 else left
            elif nums[mid] > target:
                return findLeft(low, mid - 1)
            else:
                return findLeft(mid + 1, upper)

        def findRight(low, upper):
            if low > upper:
                return -1

            mid = low + (upper - low) // 2

            if nums[mid] == target:
                right = findRight(mid + 1, upper)
                return mid if right == -1 else right
            elif nums[mid] > target:
                return findRight(low, mid - 1)
            else:
                return findRight(mid + 1, upper)

        left = findLeft(0, len(nums) - 1)
        right = findRight(0, len(nums) - 1)

        return [left, right]

            

        