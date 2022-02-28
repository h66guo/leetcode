class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i,j in enumerate(nums):
            if j != 0:
                self.vector[i] = j

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        num = 0
        for i, j in self.vector.items():
            if i in vec.vector:
                num += j*vec.vector[i]
        return num
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
