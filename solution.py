from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if (len(nums) > 2 * 10 ** 4) or (len(nums) < 1):
            raise AssertionError

        maxSoFar = minSoFar = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < -10 or nums[i] > 10:
                raise AssertionError
            curr = nums[i]
            tempMaxSoFar = max(curr, maxSoFar * curr, minSoFar * curr)
            minSoFar = min(curr, maxSoFar * curr, minSoFar * curr)
            maxSoFar = tempMaxSoFar
            result = max(maxSoFar, result)

        if result >= 2 ** 32:
            raise AssertionError

        return result
