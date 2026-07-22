class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        final = []
        altimate = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left<right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    final.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1      
                elif s<0:
                    left+=1
                else:
                    right-=1
        for e in final:
            if e not in altimate:
                altimate.append(e)
        return altimate