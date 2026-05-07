class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(low, high):
            if low > high:
                return -1
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle

            elif target < nums[middle]:
                return binarySearch(low, middle - 1)

            else:
                return binarySearch(middle + 1, high)

        return binarySearch(0, len(nums) - 1)