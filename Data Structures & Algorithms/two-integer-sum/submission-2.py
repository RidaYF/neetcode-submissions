class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapnum = {}
        ind=[]
        for i , v in enumerate(nums):
            mapnum[i]=v
    
        for k,v in mapnum.items():
            for z in range(k+1,len(mapnum)):
                if mapnum[k]+mapnum[z] == target:
                    ind.append(k)
                    ind.append(z)
                    return ind
                else:
                    continue

            
        
    