class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
            output = []
            tmp = 1
            tmpzero =[]
            ztmp=1
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] != 0 :
                        tmp *=nums[j]
                    else:
                        
                        tmpzero = nums.copy()
                        tmpzero.pop(i)
                        for e in tmpzero:
                            ztmp*=e
                        break
                if nums[i] != 0:
                    output.append(tmp//nums[i])
                    tmp=1
                else:
                     output.append(ztmp)

            return output
        