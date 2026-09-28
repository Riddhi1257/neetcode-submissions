class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range (len(nums)):
            product =1
            for j in range (len(nums)):
                if i!=j:
                    product*=nums[j]
            result.append(product)
        return result
s = Solution()
print(s.productExceptSelf([1,2,4,6]))
        