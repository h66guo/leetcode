class Solution:
    def suggestedProducts(self, products, word):
        res = []
        products.sort()
        
        for index, ch in enumerate(word):
            temp = []
            for p in products:
                if index < len(p) and p[index] == ch:
                    temp.append(p)
                    
            res.append(temp[:3])
            products = temp
            
        return res
            
