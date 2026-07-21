class Solution:
    def hasDuplicate(self, nums):
        nums.sort()
        cpt=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                cpt+=1
            else:
                continue

        if cpt>0:
            return True
        else:
            return False
    
sol = Solution()
print(sol.hasDuplicate([2, 3, 3, 5]))
            






































