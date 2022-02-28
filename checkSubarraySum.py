class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_ = 0
        modSet = {0:-1}
        for i in range(len(nums)):
            sum_ = (sum_ + nums[i]) % k
            if sum_ not in modSet:
                modSet[sum_] = i
            elif modSet[sum_] < i - 1:
                return True
        return False
