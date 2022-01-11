class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(nums, i, res): 
            seen= set()
            target=-nums[i]
            j=i+1
            while j< len(nums): 
                compliment=target-nums[j]
                if compliment in seen: 
                    res.append([nums[i], nums[j], compliment])
                    while j+1< len(nums) and nums[j]==nums[j+1]:
                        j+=1
                        
                seen.add(nums[j])
                j+=1
        res=[]
        nums.sort()
        for i in range(len(nums)): 
            if nums[i]>0: 
                break
            if i==0 or nums[i-1]!=nums[i]:
                twosum(nums, i, res)
        return res
        
