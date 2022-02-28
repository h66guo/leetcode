class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        def reverse(num, start):
            end= len(nums)-1
            while(start<end):
                temp=nums[end]
                nums[end]=nums[start]
                nums[start]=temp
                start+=1
                end-=1
            """
        Do not return anything, modify nums in-place instead.
        """
        index=len(nums) -2
        
        while index>=0 and nums[index+1]<=nums[index]:
            index-=1
        
        if index>=0:
            j=len(nums) -1
            
            while(nums[j]<=nums[index]):
                j-=1
                
            temp=nums[j]
            nums[j]=nums[index]
            nums[index]=temp
            
        reverse(nums, index+1)
        
        
