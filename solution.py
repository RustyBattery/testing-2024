from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxSoFar = minSoFar = result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            tempMaxSoFar = max(curr, maxSoFar * curr, minSoFar * curr)
            minSoFar = min(curr, maxSoFar * curr, minSoFar * curr)
            maxSoFar = tempMaxSoFar
            result = max(maxSoFar, result)

        return result
