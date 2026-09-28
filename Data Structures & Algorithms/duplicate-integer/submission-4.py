class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        for n in freq:
            if freq[n]>1:
                return True
        return False
s=Solution()
print(s.hasDuplicate([1,2,10,100,100]))
        