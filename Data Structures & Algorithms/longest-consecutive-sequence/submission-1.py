class Solution:
    def longestConsecutive(self, nums):
        nums_set=set(nums)
        longest=0

        for n in nums_set:
            if (n-1) not in nums_set:
                current=n
                length=1

                while current+1 in nums_set:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
s=Solution()
print(s.longestConsecutive([1,2,3,4,5,33,31,32,4,5]))
        