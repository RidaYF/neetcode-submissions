class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        long = []
        final = []
        altimate= []
        for e in nums:
            for n in nums:
                if e+1 == n:
                    long.append(e)
                    long.append(n)
        
            if len(nums) == 2 and nums[0] == nums[1]:
                return 1
                
        for e in long:
            if e not in final:
                final.append(e)
                
        final.sort()

        
        cpt =0
        for i in range(len(final)-1):
            
            if final[i+1] - 1 == final[i]:
                cpt+=1
            else:
                altimate.append(cpt)
                cpt=0
            altimate.append(cpt)
        print(final)
        if len(nums)==1:
            return 1
        elif len(nums) <= 0:
            return 0
        elif not altimate:
            return 1 if nums else 0
        else:
            return max(altimate)+1