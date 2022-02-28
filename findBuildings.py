class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack=[]
        index= len(heights)-1
        max_height=0
        while index>=0:
            if heights[index]>max_height:
                stack.append(index)
                max_height=heights[index]
                index-=1
                
                
            else:
                index-=1
        return sorted(stack)
            
